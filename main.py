import src.data as d
import src.neo_connection as nc

user_data = {
    "UserName": [
        "admin@my-company.com",
        "admin@my-company.com",
        "admin@my-company.com",
        "admin@my-company.com",
        "admin@my-company.com",
        "admin@my-company.com",
        "admin@my-company.com",
        "admin@my-company.com",
        "user@my-company.com",
        "user@my-company.com",
    ],
    "PermissionGroupName": [
        "Admin",
        "admin",
        "Admin",
        "Admin",
        "Admin",
        "Admin",
        "Admin",
        "Admin",
        "User",
        "User",
    ],
    "PermissionNameDescription": [
        "Add companies",
        "Add users",
        "Edit companies",
        "Edit users",
        "Delete companies",
        "Delete users",
        "View companies",
        "View Users",
        "View companies",
        "View users",
    ],
    "ResourceName": [
        "Company",
        "Users",
        "companies",
        "Users",
        "Companies",
        "Users",
        "Companies",
        "users",
        "Companies",
        "User",
    ],
    "AccessLevelName": [
        "add",
        "Add",
        "Edit",
        "Edit",
        "delete",
        "Delete",
        "View",
        "View",
        "view",
        "View",
    ],
    "CompanyName": [
        "My Company",
        "My Company",
        "My Company",
        "My Company",
        "My Company",
        "My Company",
        "My Company",
        "My Company",
        "My Company",
        "My Company",
    ],
}

create_data_df = d.create_data(user_data)

d.export_data(create_data_df, "data/data.csv")

nc.create_user("test@my-company.com", 1)

nc.create_company("Test Company")

nc.create_permission_group("Super User")

nc.return_users()
