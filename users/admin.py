# user_app/admin.py
from django.contrib import admin
from .models import User  # or whatever your model is

admin.site.register(User)
