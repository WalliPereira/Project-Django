from django.contrib import admin
from students.models import Student,Courses

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'lastname')

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Student,StudentAdmin)

# Register your models here.
