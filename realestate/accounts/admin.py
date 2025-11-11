from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Unregister the default User (prevents AlreadyRegistered error)


# Re-register User with the default UserAdmin
admin.site.register(User, UserAdmin)

# Register any other models from your accounts app below
# from .models import Profile
# admin.site.register(Profile)
admin.site.register(Account)