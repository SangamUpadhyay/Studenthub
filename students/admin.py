from django.contrib import admin
from .models import Student

# ModelAdmin class create karo
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'mobile_No', 'full_name', 'father_name', 'mother_name', 'student_id', 'state', 'city','country')  # columns jo admin me dikhne chahiye
    list_display_links = ('username',)  # username par click karke detail view open ho
    search_fields = ('username', 'email','id')  # search bar me search karne ke liye

# Model register karo with custom admin
admin.site.register(Student, StudentAdmin)