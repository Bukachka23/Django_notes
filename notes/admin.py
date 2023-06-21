from django.contrib import admin
from .models import Category, Note

# Register the Category and Note models with Django's admin interface
# This allows you to perform CRUD operations on these models from the admin interface
admin.site.register(Category)
admin.site.register(Note)
