from django.shortcuts import render,redirect
from Site_admin.models import *
from django.contrib import messages



def studentHome(request):
    return render(request,'student/home.html')


def student_exam(request):
    id=request.session['studentid']
    student=Student.objects.filter(id=id)
    seating_details=Seating_Arrangement.objects.filter(studentid=id).select_related('examid','hallid')
    exams_with_seating = []
    for seating in seating_details:
        # Get all exams that are scheduled on the same date as the seating arrangement
        exams = Exam.objects.filter(Date=seating.examid,Semester=student[0].Semester)  # Get all exams on that exam date
        for exam in exams:
            exams_with_seating.append((seating, exam))

    return render(request, 'student/seating_details.html', {'exams_with_seating': exams_with_seating})


def student_profile(request):
    student=Student.objects.filter(id=request.session['studentid'])
    return render(request,'student/profile.html',{'stu':student})

def student_change(request):
    if request.method == "POST":
        id=request.session['studentid']
        student=Student.objects.filter(id=id)
        old_fromdb=Login_tb.objects.filter(id=student[0].Loginid.id)
        old_pass=old_fromdb[0].Password
        old=request.POST['old_pass']
        new=request.POST['new_pass']
        if(old==old_pass):
            Login_tb.objects.filter(id=old_fromdb[0].id).update(Password=new)
            messages.success(request,"Password updated")
            return render(request,'common/login.html')
        else:
            messages.error(request,"old password is wrong")
            return render(request,'student/changepass.html')
    return render(request,'student/changepass.html')