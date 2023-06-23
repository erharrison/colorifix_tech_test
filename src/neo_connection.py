from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = "neo4j+s://e1345022.databases.neo4j.io"

class Permission(StructuredNode):
    id = UniqueIdProperty()
    name = StringProperty(required=True)

class AccessLevel(StructuredNode):
    id = UniqueIdProperty()
    name = StringProperty(required=True)

class Company(StructuredNode):
    id = UniqueIdProperty()
    name = StringProperty(required=True)

class User(StructuredNode):
    id = UniqueIdProperty()
    name = StringProperty(required=True)
    copmanyId = IntegerProperty(required=True)

    company = RelationshipTo(Company, 'BELONGS_TO')

class Resource(StructuredNode):
    id = UniqueIdProperty()
    name = StringProperty(required=True)

class Request(StructuredNode):
    id = UniqueIdProperty()
    userId = IntegerProperty(required=True)
    permissionId = IntegerProperty(required=True)
    resourceId = IntegerProperty(required=True)
    accessLevelId = IntegerProperty(required=True)
    companyId = IntegerProperty(required=True)

    user = RelationshipTo(User, 'REQUEST_BY')
    resource = RelationshipTo(User, 'REQUEST_RESOURCE')
    permission = RelationshipTo(User, 'REQUEST_PERMISSION')
    access_level = RelationshipTo(User, 'REQUEST_ACCESS_LEVEL')
    company = RelationshipTo(User, 'REQUEST_TARGET_COMPANY  ')
