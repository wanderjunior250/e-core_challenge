*** Settings ***
| Resource       | ../resources/support/index.robot
| Suite Setup    | Before
| Suite Teardown | After
| Test Setup     | Background: Login


*** Test Cases ***
| Scenario: Valid Login
| | [Template]   | Scenario: Valid Login
| | VALID_USER_1

| Scenario Outline: Invalid Login
| | [Template]   | Scenario Outline: Invalid Login
| | INVALID_USER_1
| | INVALID_USER_2
| | INVALID_USER_4
| | INVALID_USER_4
| | INVALID_USER_5


*** Keywords ***
| Background: Login
| | Given the user is on the login_page

| Scenario: Valid Login
| | [Arguments]  | ${user}
| | When the user ${user} tries to login
| | Then the user should be logged in
| | And the user do logout

| Scenario Outline: Invalid Login
| | [Arguments]  | ${user}
| | When the user ${user} tries to login
| | Then the user should not be logged in