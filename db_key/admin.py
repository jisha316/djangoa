from django.contrib import admin

from db_key.models import course,student

# Register your models here.

admin.site.register(course)
admin.site.register(student)

from django.contrib import admin
from.models import course
from.models import student


# @admin.register(course)
# class courseAdmin(admin.ModelAdmin):
#     list_display = ('course_name','fee')

# @admin.register(student)
# class studentAdmin(admin.ModelAdmin):
#     list_display = ('id','course_name','address','email','age','join_date')






