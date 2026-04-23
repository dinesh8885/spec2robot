from robot.api import logger
from robot.api.deco import keyword
from datetime import datetime
# Global list to store log messages
log_messages = []
current_time = datetime.now()
class LiveExecutionListener:
    ROBOT_LISTENER_API_VERSION = 2

    def start_suite(self, name):
        msg = f"Starting suite: {name}"
        log_messages.append(msg)
        logger.info(msg)

    def end_suite(self, name, attrs):
        msg = f"Ending suite: {name} with status: {attrs['status']}"
        log_messages.append(msg)
        logger.info(msg)

    def start_test(self, name):
        msg = f"Starting test: {name}"
        log_messages.append(msg)
        logger.info(msg)

    def end_test(self, name, attrs):
        msg = f"Ending test: {name} with status: {attrs['status']}"
        log_messages.append(msg)
        logger.info(msg)

    def log_message(self, message1=None, message2=None, message3=None):
        msg = f" {current_time.strftime('%Y-%m-%d %H:%M:%S')}{'----->'}{message1}    {message2 if message2 else ''}    {message3 if message3 else ''}"
        log_messages.append(msg)
        logger.console(msg)  # Pint to the console as well

    def close(self):
        msg = "Test execution completed."
        log_messages.append(msg)
        logger.info(msg)

# This is the keyword that will be used in the tests
@keyword(name="Get Live Log Messages")
def get_live_log_messages():
    return log_messages
