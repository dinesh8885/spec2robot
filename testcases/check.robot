*** Settings ***
Library     OperatingSystem
Library     String
Library     ../lib/testkeywords.py

*** Test Cases ***
Test Case 1
    [Setup]    Setup Test Case 1
    [Teardown]    Teardown Test Case 1
    Perform Load test
    Validate the basic functionality
Test Case 2
    [Setup]    Setup Test Case 2
    [Teardown]    Teardown Test Case 2
    increase temperature
    perform basic functionality

*** Keywords ***
Setup Test Case 1
    Turn on the Power supply
    Send Ignition signal
    Validate the response
Teardown Test Case 1
    Turn off the signal
    Send Ignition off signal
Setup Test Case 2
    Turn on the power supply
    Trigger wakeup signal
    DUT should be up
Teardown Test Case 2
    Turn off the power supply
    DUT should be turned off
    current consumption should be zero
