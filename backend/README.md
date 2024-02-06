# LASS Backend
## Setup
### Virtual Environment
Main purpose of a virtual environment is to ensure we are using the same version of libraries, and to avoid dependency issues that arise with installing different versions of the same package.
- Get a virtual environment:
    - `python3 -m venv venv`
- Activate virtual environment:
    - Windows: `.\venv\Scripts\activate`
    - Unix: `source venv/bin/activate`
- Install requirements in environment only:
    - `python3 -m pip install -r requirements.txt`
- Now you can develop and test, to run dev server:
    - `python3 app.py`
- To deactivate when done:
    - `deactivate`
- To add a new library/import while in the virtual environment:
    - `python3 -m pip install <library>`
    - `python3 -m pip freeze > requirements.txt`

## Unit Tests/Functional (Integration) Tests
Here is a resource [on the difference between Unit and Functional Tests, and more about Flask unit testing!](https://testdriven.io/blog/flask-pytest/#what-to-test)

- Run all tests:
    - `python3 -m pytest`
- Run a folder of tests:
    - `python3 -m pytest tests/unit`
- Run tests in a file:
    - `python3 -m pytest tests/functional/test_example.py`
- Run specific test function:
    - `python3 -m pytest tests/unit/test_example.py::test_func`