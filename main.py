import src.data as d

user_data = d.Data([
    "UserName",
    "PermissionGroupName",
    "PermissionNameDescription",
    "ResourceName",
    "AccessLevelName",
    "CompanyName"
],
    [["admin@my-company.com", "Admin", "Add companies", "Company", "add", "My Company"],
     ["admin@my-company.com", "admin", "Add users", "Users", "Add", "My Company"],
     ["admin@my-company.com", "Admin", "Edit companies", "companies", "Edit", "My Company"],
     ["admin@my-company.com", "Admin", "Edit users", "Users", "Edit", "My Company"],
     ["admin@my-company.com", "Admin", "Delete companies", "Companies", "delete", "My Company"],
     ["admin@my-company.com", "Admin", "Delete users", "Users", "Delete", "My Company"],
     ["admin@my-company.com", "Admin", "View companies", "Companies", "View", "My Company"],
     ["admin@my-company.com", "Admin", "View Users", "users", "View", "My Company"],
     ["user@my-company.com", "User", "View companies", "Companies", "view", "My Company"],
     ["user@my-company.com", "User", "View users", "User", "View", "My Company"]]
)

create_data_df = d.Data.create_data()
print(create_data_df)
