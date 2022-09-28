from django.contrib import admin

from .models import (Course, MainCourses)

admin.site.register(
    Course)
admin.site.register(
    MainCourses)

