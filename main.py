from configparser import ConfigParser
from pathlib import Path
from subprocess import run

from flask import Flask, jsonify
from flask_apscheduler import APScheduler
from requests import post

from lib.listener import get_live_log_messages
from lib.testcase_generator import testcase_generator

BASE_DIR = Path(__file__).resolve().parent
TESTCASE_DIR = BASE_DIR / "testcases"
RESULTS_DIR = BASE_DIR / "results"

app = Flask(__name__)
scheduler = APScheduler()


class AppConfig:
    def __init__(self, config_file=BASE_DIR / "config.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get(self, option, fallback=None):
        return self.config.get("DEFAULT", option, fallback=fallback)

    def get_bool(self, option, fallback=False):
        raw_value = self.get(option, str(fallback))
        return str(raw_value).strip().strip('"').lower() in {"true", "1", "yes", "on"}

    def get_int(self, option, fallback=1200):
        return self.config.getint("DEFAULT", option, fallback=fallback)


config_obj = AppConfig()


class SchedulerService:
    def __init__(self):
        self.logs = get_live_log_messages()

    def scheduled_task(self):
        interval = config_obj.get_int("SECONDS", 1200)
        print(f"Running scheduled asset sync every {interval} seconds.")
        self.generate_test_case()

    def generate_test_case(self):
        generator = testcase_generator()
        TESTCASE_DIR.mkdir(exist_ok=True)

        for xls_file in self.get_asset_files(".xlsx"):
            output_file = TESTCASE_DIR / f"{xls_file.stem}.robot"
            generator.parse_excel_to_robot(str(xls_file), str(output_file))

        for xml_file in self.get_asset_files(".xml"):
            test_cases = generator.parse_xml(str(xml_file))
            if test_cases:
                output_file = TESTCASE_DIR / f"{xml_file.stem}.robot"
                generator.generate_robotframework_testcase(test_cases, str(output_file))

        self.start_test(TESTCASE_DIR)

    def get_asset_files(self, suffix):
        files = []
        for file_path in BASE_DIR.iterdir():
            if file_path.suffix.lower() != suffix:
                continue
            if suffix == ".xlsx" and file_path.name.startswith("~$"):
                continue
            files.append(file_path)
        return sorted(files)

    def start_test(self, path):
        listener_path = BASE_DIR / "lib" / "listener.py"
        RESULTS_DIR.mkdir(exist_ok=True)

        command = [
            "robot",
            "--listener",
            str(listener_path),
            "-d",
            str(RESULTS_DIR),
            str(path),
        ]
        try:
            completed = run(command, capture_output=True, text=True, cwd=BASE_DIR, check=False)
            combined_logs = [line for line in (completed.stdout + "\n" + completed.stderr).splitlines() if line]
            self.logs = combined_logs or ["Robot execution completed without console output."]
        except FileNotFoundError:
            self.logs = ["Robot Framework CLI is not installed or not available in PATH."]


service = SchedulerService()
scheduler.init_app(app)


@app.route("/")
def home():
    return jsonify(
        {
            "project": "Spec2Robot",
            "message": "Asset-driven Robot Framework test generation service is running.",
            "supported_inputs": [".xlsx", ".xml"],
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/status")
def status():
    return jsonify(service.logs)


@app.route("/trigger")
def intermediate_trigger():
    service.scheduled_task()
    return jsonify({"message": "Test case generation triggered"})


@app.route("/send_data")
def send_data():
    url = config_obj.get("URL")
    if not url:
        return jsonify({"error": "URL is not configured in config.ini"}), 400

    response = post(url, json={"logs": service.logs}, timeout=30)
    return jsonify({"status_code": response.status_code, "response": response.text})


def bootstrap_scheduler():
    if scheduler.get_job("scheduled-task") is None:
        scheduler.add_job(
            id="scheduled-task",
            func=service.scheduled_task,
            trigger="interval",
            seconds=config_obj.get_int("SECONDS", 1200),
        )

    if config_obj.get_bool("SCHEDULER_ENABLED", True) and not scheduler.running:
        scheduler.start()


bootstrap_scheduler()
service.scheduled_task()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
