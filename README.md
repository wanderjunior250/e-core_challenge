# Robot GUI Automation E-Core Challenge

This project has the goal of being an example of an automated testing structure using Robotframework in Python, also has
implementation of the design pattern page objects for the e-core challenge.

The project uses BDD to write test scenarios and it's structure was constructed to be similar with Cucumber implementation.

## Requirements

You'll need to install the following:
- Python 2.7.x
- Selenium webdriver (e.g. chromedriver) on the Python instalation path (/bin) 

## Installation

Run the the following command line in the project root path:

```python
$ pip install -r requirements.txt 
```

## Running the project

There's a simple way of running all the tests scenarios:

```python
$ robot --outputdir reports --pythonpath resources/pages tests 
```

## Continuous Improvement
Some small points can improve the quality and maturity of this automation:
- Add a webdriver manager to handle different browser execution and different versions of the webdriver as it will use the right one according to the browser version on the machine;
- All command lines can be encapsulated using python invoke task manager, in order to facilitate CI/CD and have different configurations in a single place for the executions;


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)