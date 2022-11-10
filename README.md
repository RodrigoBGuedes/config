
# Config
Config is an application used to create Appointments between two objects.

## Installing Poetry
This project uses poetry to do the management of packages and virtual environments. 
If Poetry is not already installed in your computer, follow this steps:
[Poetry Instruction Page](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Commands to run when the poetry is installed:
To create a virtual environment and install the tools in pyproject.toml run:
```bash
poetry install
```

To activate the virtual environment run:
```bash
poetry shell
```

You can run the server using:
```bash
poetry run python manage.py runserver
```