from listener import LiveExecutionListener

class testkeywords:
    
    def __init__(self):
        self.logger=LiveExecutionListener()
        self.logger.start_suite("Test Suite")
    
    def Send_Signal(self, signal, value):
        self.logger.log_message("send signal", signal, value)
        return True
    
    def Get_Signal(self, signal,value):
        self.logger.log_message("get signal", signal,value)
        return True
    
    def PPS_OFF(self):
        self.logger.log_message("PPS OFF")
        return True
    
    def PPS_ON(self):
        self.logger.log_message("PPS ON")
        return True
    
    def Turn_on_the_Power_supply(self):
        self.logger.log_message("Turn on the Power supply")
        return True
    
    def Send_Ignition_Signal(self):
        self.logger.log_message("Send Ignition Signal")
        return True
    
    def Validate_the_response(self):
        self.logger.log_message("Validate ignition status")
        return True
    
    def Turn_off_the_signal(self):
        self.logger.log_message("Turn off the signal")
        return True
    
    def Perform_Load_test(self):
        self.logger.log_message("Perform Load test")
        return True
    
    def validate_the_basic_functionality(self):
        self.logger.log_message("Validate the basic functionality")
        return True
    
    def increase_temperature(self):
        self.logger.log_message("Increase temperature")
        return True
    
    def perform_basic_functionality(self):
        self.logger.log_message("Perform basic functionality test")
        return True
    
    def send_ignition_off_signal(self):
        self.logger.log_message("Send ignition off signal")
        return True
    
    def trigger_wakeup_signal(self):
        self.logger.log_message("Trigger wakeup signal")
        return True
    
    def dut_should_be_up(self):
        self.logger.log_message("DUT should be up")
        return True
    
    def Turn_off_the_power_supply(self):
        self.logger.log_message("Turn off the power supply")
        return True
    
    def DUT_should_be_turned_off(self):
        self.logger.log_message("DUT should be down")
        return True
    
    def current_consumption_should_be_zero(self):
        self.logger.log_message("Current consumption should be less than 0")
        return True