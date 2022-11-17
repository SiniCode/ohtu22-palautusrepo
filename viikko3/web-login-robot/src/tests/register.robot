*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Open Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ap
    Set Password  hamahakk1
    Confirm Password  hamahakk1
    Submit Credentials
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  nalle
    Set Password  puh0
    Confirm Password  puh0
    Submit Credentials
    Registration Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  nalle
    Set Password  puuskupuh0
    Confirm Password  puhvelielain0
    Submit Credentials
    Registration Should Fail With Message  Passwords do not match


*** Keywords ***
Reset Application And Open Register Page
    Reset Application
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registration Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}        
