*** Settings ***
| Resource       | ../resources/support/index.robot
| Suite Setup    | Before
| Suite Teardown | After
| Test Setup     | Background: Login


*** Test Cases ***
| Scenario: TC001 - Login (Positive)
| | [Template]   | Valid Login
| | VALID_USER_1

| Scenario Outline: TC002 - Login (Negative)
| | [Template]   | Invalid Login
| | INVALID_USER_1
| | INVALID_USER_2
| | INVALID_USER_3
| | INVALID_USER_4
| | INVALID_USER_5


*** Keywords ***
| Background: Login
| | Given the user is on the login_page

| Valid Login
| | [Arguments]  | ${user}
| | When the user ${user} tries to login
| | Then the user should be logged in
| | And the user do logout

| Invalid Login
| | [Arguments]  | ${user}
| | When the user ${user} tries to login
| | Then the user should not be logged in