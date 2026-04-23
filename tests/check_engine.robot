*** Settings ***
Library     OperatingSystem
Library     String

*** Test Cases ***
Check Ignition wih Left Indicator
   [Documentation]    Turn on the Power supply
    ...               Send Ignition signal ON
    ...               Perform set signal left indicator
    ...               Check Left Indicator
    ...               Send Ignition signal OFF
    ...               Perform set signal left indicator
    ...               Turn off the Power supply
   [Setup]     PPS_ON            

   Send_Signal    Igntion_cyc    0x4    
   Send_Signal    turn_left_ind    0x1    
   Get_Signal    turn_left_ind    0x1    

   [Teardown]     Send_Signal    Igntion_cyc    0x0    
                  Send_Signal    turn_left_ind    0x1    
                  PPS_OFF            


Check Ignition wih Right Indicator
   [Documentation]    Turn on the Power supply
    ...               Send Ignition signal ON
    ...               Perform set signal Right indicator
    ...               Check Right Indicator
    ...               Turn off the Power supply
   [Setup]     PPS_ON            

   Send_Signal    Igntion_cyc    0x4    
   Send_Signal    turn_left_ind    0x1    
   Get_Signal    turn_left_ind    0x1    

   [Teardown]     Send_Signal    Igntion_cyc    0x0    


Check Speed Signal at Low Speed
   [Documentation]    Turn on the Power supply
    ...               Send Ignition signal ON
    ...               Set Speed signal to 30 km/h
    ...               Check Speed Indicator
    ...               Send Ignition signal OFF
    ...               Reset Speed signal
    ...               Turn off the Power supply
   [Setup]     PPS_ON            

   Send_Signal    Igntion_cyc    0x4    
   Send_Signal    speed_signal    0x1E    
   Get_Signal    speed_signal    0x1E    

   [Teardown]     Send_Signal    Igntion_cyc    0x0    
                  Send_Signal    speed_signal    0x0    
                  PPS_OFF            


Check Speed Signal at High Speed
   [Documentation]    Turn on the Power supply
    ...               Send Ignition signal ON
    ...               Set Speed signal to 100 km/h
    ...               Check Speed Indicator
    ...               Send Ignition signal OFF
    ...               Reset Speed signal
    ...               Turn off the Power supply
   [Setup]     PPS_ON            

   Send_Signal    Igntion_cyc    0x4    
   Send_Signal    speed_signal    0x64    
   Get_Signal    speed_signal    0x64    

   [Teardown]     Send_Signal    Igntion_cyc    0x0    
                  Send_Signal    speed_signal    0x0    
                  PPS_OFF            


Check Ignition Signal with Engine Start
   [Documentation]    Turn on the Power supply
    ...               Send Ignition signal ON
    ...               Start Engine
    ...               	Check Engine Running Signal
    ...               Send Ignition signal OFF
    ...               Stop Engine	
    ...               Turn off the Power supply
   [Setup]     PPS_ON            

   Send_Signal    Igntion_cyc    0x4    
   Send_Signal    Igntion_cyc    0x1    
   Get_Signal    Igntion_cyc    0x1    

   [Teardown]     Send_Signal    Igntion_cyc    0x0    
                  Send_Signal    engine_start    0x0    
                  PPS_OFF            

