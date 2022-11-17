*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  nalle  hunajata456
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  3loikkanen
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ap  hamahakk1
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  nalle  puh0
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  nalle  puhjapuolihehtaaria
    Output Should Contain  Password must contain numbers or special characters


*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
