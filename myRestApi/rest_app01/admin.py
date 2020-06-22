from django.contrib import admin
from rest_app01.models.school import School

# Register your models here.


@admin.register(School)
class SchoolManager(admin.ModelAdmin):
    list_display = ['id', 'avatar', 'name']

