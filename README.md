# colorifix_tech_test

### Installation Guide


### Assumptions
* A user can only belong to one company, but can access resources from multiple companies.

### TODO List
* Include black in repo CI/CD, to auto validate PEP8
* Unit tests
* Use OOP
* Error Handling
* Add constraints to nodes in neo_connection.py to ensure foreign key ID's correspond to existing Primary keys in appropriate tables
* Test connection to Neo4j and ensure functions for interacting with it are working as expected

### Issues Encountered / Future Plans
* Familiarising myself with Neo4j, and how to interact with it using Python
* Familiarising myself with normalisation
* The way I have designed the database, the permissions of a user can't be edited. I assumed a user can have multiple permissions, depending on the company they are making a request to, so linked permission to the request itself
* Connection to Neo4j database not currently working, couldn't resolve error in time
* I intended to implement the django framework, to interact with my Neo4j database, but wanted to experiment with neo