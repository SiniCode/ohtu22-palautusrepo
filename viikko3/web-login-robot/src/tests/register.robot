*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Open Register Page


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123  kalle123
    Click Register Button
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Input Credentials  ap  hamahakk1  hamahakk1
    Click Register Button
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  nalle  puh0  puh0
    Click Register Button
    Registration Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Input Credentials  nalle  puuskupuh0  puhvelielain0
    Click Register Button
    Registration Should Fail With Message  Passwords do not match

Login After Successful Registration
    Input Credentials  kalle  kalle123  kalle123
    Click Register Button
    Registration Should Succeed
    Go To Login Page
    Page Should Contain  Login
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Input Credentials  nalle  puh  puh
    Click Register Button
    Registration Should Fail With Message  Password is too short
    Go To Login Page
    Page Should Contain  Login
    Set Username  nalle
    Set Password  puh
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Reset Application And Open Register Page
    Reset Application
    Go To Register Page
    Register Page Should Be Open

Set New Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set New Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm New Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Input Credentials
    [Arguments]  ${username}  ${password1}  ${password2}
    Set New Username  ${username}
    Set New Password  ${password1}
    Confirm New Password  ${password2}

Click Register Button
    Click Button  Register

Registration Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}        
