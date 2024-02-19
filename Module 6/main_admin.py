# Written by Tiago Perez

from user_admin import Admin

admin_privileges = [
    "can add post",
    "can delete post",
    "can ban user",
    "can modify user profile"
]

admin_user = Admin("Admin", "User", "admin", "Headquarters", admin_privileges)

admin_user.privileges.show_privileges()
