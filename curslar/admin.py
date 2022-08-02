from django.contrib import admin
from .models import *


class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_solved']


admin.site.register(Courses)
admin.site.register(Contact, AdminContact)
