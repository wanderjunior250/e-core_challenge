*** Settings ***
| Resource       | ../resources/support/index.robot
| Suite Setup    | Before
| Suite Teardown | After
| Test Setup     | Background: Valid Login | VALID_USER_1


*** Test Cases ***
| Scenario Outline: TC003 - Validate invoice detail
| | [Template]   | Check Invoice Details
| | INVOICE_1


*** Keywords ***
| Background: Valid Login
| | [Arguments]  | ${user}
| | Given the user is on the login_page
| | When the user ${user} tries to login
| | Then the user should be logged in

| Check Invoice Details
| | [Arguments]  | ${invoice}
| | When the user click invoice details for the first item
| | Then the application should open invoice details screen
| | And the information presented should match ${invoice}