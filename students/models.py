from django.db import models


class Student(models.Model):

    # Account Details
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    # Personal Details
    first_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)

    full_name = models.CharField(max_length=200)
    # Student Details
    student_id = models.CharField(max_length=20, unique=True)
    mobile_No = models.CharField(max_length=10)

    # Address Details
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username