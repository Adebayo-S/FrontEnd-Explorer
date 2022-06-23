## working in a virtual environment

> py -3 -m venv venv
> venv\Scripts\activate

## Using Flask

### In bash terminal

- export FLASK_APP=Flask
- export FLASK_ENV=development (whenever we make mods, the server restarts)
- flask run

### In powershell terminal

- $env:FLASK_APP = "flaskr"
- $env:FLASK_ENV = "development"
- flask run
