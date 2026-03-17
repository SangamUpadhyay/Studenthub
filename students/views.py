from django.shortcuts import render, redirect
from .models import Student 
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def add_student(request):
    if request.method == "POST":
        username =request.POST.get('username')
        email =request.POST.get('email')
        password =request.POST.get('password')
        confairm_password =request.POST.get('confirm_password')

        if password==confairm_password:


            Student.objects.create(username=username, email=email, password=password)
            messages.success(request, 'Student added successfully!')

        else:
            messages.error(request, 'Passwords do not match!')

        return redirect('add_student') 

    students = Student.objects.all()

    return render(request, 'addstudents.html', {'students': students})


def student_list(request):
    if request.method == "POST":
        id =request.POST.get('id')
        username =request.POST.get('username')
        email =request.POST.get('email')
        Mobile_No =request.POST.get('Mobile_No')

        Student.objects.create(username=username, email=email, Mobile_No=Mobile_No)
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(username=username, password=password)

            # session में student id save
            request.session['student_id'] = student.id

            return redirect("student_profile")

        except Student.DoesNotExist:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")

def student_profile(request):

    student_id = request.session.get('student_id')

    if not student_id:
        return redirect("login")

    student = Student.objects.get(id=student_id)

    if request.method == "POST":

        first_name = request.POST.get("first_name", "")
        middle_name = request.POST.get("middle_name", "")
        last_name = request.POST.get("last_name", "")

        student.full_name = f"{first_name} {middle_name} {last_name}".strip()

        student.father_name = request.POST.get("father_name")
        student.mother_name = request.POST.get("mother_name")
        student.mobile_No = request.POST.get("mobile_No")
        student.student_id = request.POST.get("student_id")
        student.state = request.POST.get("state")
        student.city = request.POST.get("city")
        student.country = request.POST.get("country")

        student.save()
        messages.success(request, "Profile updated successfully!")

    return render(request, "student_profile.html", {"student": student})