*** Settings ***
Documentation     RestAssured API Testing
...
...               Keywords are imported from the resource file
Default Tags      positive  start
Library           Collections
Library           lib.py

*** Variables ***
@{ROBOTS}=        Bender    Johnny5    Terminator    Robocop
${count}          1
${status}       Pending
*** Keywords ***
Foobar
    ${VALUE}    Evaluate    ${VALUE} + 1
    Log To Console  ${VALUE}
    Set Test Variable    ${VALUE}
    [Return]    ${VALUE}


*** Test Cases ***

TC_001
    @{ITEMS} =  Create List  Item 1  Item 2  Item 3
    FOR     ${x}    IN      zero_to_infinity
    Log To Console  ${x}
    Log To Console   Hello
    Set Variable    ${ITEMS}
    Run Keyword If  "${count}" == "10"  Exit For Loop
    ${x}    Evaluate  ${count} + 1
    END


example
    @{VALUE}
    Set Test Variable      ${VALUE}      0
    Do While Loop    Foobar     ${VALUE}


