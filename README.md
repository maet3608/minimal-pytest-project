# minimal-pytest-project

Example and template for a minimal project with pytest support.


## Documentation

- [pytest](http://pytest.org)
- [pytest-cov](https://pypi.python.org/pypi/pytest-cov)


## Installation

### pytest

```pip install pytest``` or ```conda install pytest```

### pytest-cov

```pip install pytest-cov``` or ```conda install pytest```

create file .coveragerc with following content:
```
[run]
omit = tests/*,*/__init__.py,*/test_*
```

## Run tests

```
pytest                           // runs all tests in all folders recursively
pytest -v                        // verbose output

pytest -k test_add               // specific test
pytest tests                     // specific test package
pytest tests/test_calculator.py  // specific test module

pytest --duration=3              // profiling of 3 slowest (test) functions
pytest --doctest-modules         // run doctests
```

### Set default flags for test run

create file pytest.ini with following content to always run doctests
```
[pytest]
addopts = --doctest-modules
```

## Get coverage

```
pytest --cov
pytest --cov=mymath
pytest --cov=mymath --cov-report html
```