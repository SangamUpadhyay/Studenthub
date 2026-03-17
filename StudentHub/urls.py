
from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('studentslist/', views.student_list, name='student_list'),
    path('login/', views.login, name='login'),
    path('profile/', views.student_profile, name='student_profile'),

]
