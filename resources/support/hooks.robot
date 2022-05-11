*** Keywords ***
| Before
| | ${mass}                   | config.Mass
| | ${env}                    | config.Env
| | Set Global Variable       | ${MASS}                   | ${mass}
| | Set Global Variable       | ${ENV}                    | ${env}
| | Open Browser              | about:blank               | chrome
| | Maximize Browser Window
| | Go To                     | ${ENV['App']['url']}

| After
  Close Browser

| Before Each
# if needed

| After Each
# if needed (e.g. taking screenshots)