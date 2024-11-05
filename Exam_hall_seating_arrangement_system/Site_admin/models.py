from django.db import models
from django.contrib.auth.models import User

class Admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class Course(models.Model):
    course=models.CharField(max_length=20)


class Subject(models.Model):
    courseid=models.ForeignKey(Course,on_delete=models.CASCADE)
    subject=models.CharField(max_length=20)

class Login_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    User_type=models.CharField(max_length=20)

class Teacher(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Subjectid=models.ForeignKey(Subject,on_delete=models.CASCADE)
    Contact=models.CharField(max_length=20)
    Email=models.EmailField()
    Loginid=models.ForeignKey(Login_tb,models.CASCADE)




class Student(models.Model):
    Register_number=models.CharField(max_length=20)
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Department=models.CharField(max_length=20)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Semester=models.CharField(max_length=20)
    Mobile=models.CharField(max_length=20)
    Image=models.ImageField(null=True,blank=True)
    Address=models.CharField(max_length=20)
    Email=models.EmailField()
    Loginid=models.ForeignKey(Login_tb,models.CASCADE)
    
class Hall(models.Model):
    Hall_no=models.CharField(max_length=20)
    Capacity=models.PositiveIntegerField()


class Exam_date(models.Model):
    Date_of_exam=models.DateField()

class Exam(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    Date=models.ForeignKey(Exam_date,on_delete=models.CASCADE)
    Time=models.TimeField()
    Duration=models.CharField(max_length=20)
    Semester=models.CharField(max_length=20)

class Seating_Arrangement(models.Model):
    examid=models.ForeignKey(Exam_date,on_delete=models.CASCADE)
    hallid=models.ForeignKey(Hall,on_delete=models.CASCADE)
    studentid=models.ForeignKey(Student,on_delete=models.CASCADE)
    seat_no=models.PositiveIntegerField()


class Allocation(models.Model):
    Date=models.ForeignKey(Exam_date,on_delete=models.CASCADE)
    Subject_ids=models.CharField(max_length=100)
    Shift=models.CharField(max_length=20)
    Invigilator_name=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    Hallid=models.ForeignKey(Hall,on_delete=models.CASCADE)