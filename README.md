# colorifix_tech_test

## Installation Guide

### Virtual Environment
With poetry installed, create a virtual environment with poetry in a way that works for the development environment 
you're using (refer to this [guide](https://python-poetry.org/docs/)). 
Then run this command in your terminal:

```
poetry install
```

Note that if the poetry executable hasn't been added to your PATH variable, you will need to point the command towards
the location of the poetry executable on your device. Here's an example of what that could look like:

```
C:\Users\user.name\path\to\poetry install
```

This command should install the dependencies outlined in the `pyproject.toml` file in the root project folder, 
and recreate the `poetry.lock` file.

### Running project
Executing `main.py` in the project root runs the appropriate functions in the `src\` folder for the technical test.
Execute this command from the root of the project to run it:

```
poetry run .\main.py
```

Note that this currently only creates a `data.csv` file in the `data\` folder. The rest of the functionality is still
in development, so currently the database can't be altered or read from using this project.

## Assumptions
* A user can only belong to one company, but can access resources from multiple companies.
* A user can have different permission levels based on the company they are accessing resources for.

## TODO List
* Auto validate PEP8 standards in git CI/CD.
* Unit tests.
* Use OOP.
* Error Handling.
* Add constraints to nodes in neo_connection.py to ensure foreign key ID's correspond to existing Primary keys in
appropriate tables.
* Create a connection to Neo4j and ensure functions for interacting with it are working as expected.
* Tidy up data, so that the same values are spelled the same e.g. admin changed to Admin

## Issues Encountered / Future Plans
* Familiarising myself with Neo4j, and how to interact with it using Python.
* Familiarising myself with normalisation.
* The way I have designed the database, the permissions of a user can't be edited. I assumed a user can have multiple
permissions, depending on the company they are making a request to, so linked permission to the request itself.
* Connection to Neo4j database not currently working, didn't resolve error in time.
* I intended to implement the django framework, to interact with my Neo4j database.