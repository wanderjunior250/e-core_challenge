*** Keywords ***
| the user is on the login_page
| | Go to page | LoginPage

| the user ${x} tries to login
| | Set Test Variable  |  ${user}  | ${x}
| | Do login           |  ${user}

| the user should be logged in
| | The current page should be | HomePage

| the user do logout
| | Go To              | ${ENV['App']['url']}/logout

| the user should not be logged in
| | The current page should be | LoginPage
| | Check login error message