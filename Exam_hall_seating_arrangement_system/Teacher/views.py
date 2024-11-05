from django.shortcuts import render
from Site_admin.models import *
from django.core.paginator import Paginator
from django.contrib import messages

def teacherHome(request):
    return render(request,'teacher/home.html')

def teacher_exam(request):
    id=request.session['teacherid']
    allocation = Allocation.objects.filter(Invigilator_name=id)
    
    # Split the comma-separated subject IDs
    subject_ids = allocation[0].Subject_ids.split(',')
    
    # Query the Subject model to fetch the subjects with those IDs
    subjects = Subject.objects.filter(id__in=subject_ids)
    
    # Get the subject names and join them with commas
    subject_names = ", ".join([subject.subject for subject in subjects])
    p=Paginator(allocation,2)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    
    return render(request,'teacher/exam_details.html',{'all':page_obj,'subject':subject_names})

def teacher_exam_details(request):
    id=request.GET['ex']
    allocation=Allocation.objects.filter(id=id)
    subject_ids=allocation[0].Subject_ids.split(',')
    subjects=Subject.objects.filter(id__in=subject_ids)
    exams = Exam.objects.filter(subject__in=subjects).distinct()
    return render(request,'teacher/exam_details_partial.html',{'exam':exams})

def teacher_seating(request,Hallid,Dateid):
    seating=Seating_Arrangement.objects.filter(hallid=Hallid,examid=Dateid)
    return render(request,'teacher/seating_partial.html',{'seat':seating})

def teacher_profile(request):
    id=request.session['teacherid']
    teacher=Teacher.objects.filter(id=id)
    return render(request,'teacher/profile.html',{'te':teacher})

def teacher_change(request):
    if request.method == "POST":
        id=request.session['teacherid']
        teacher=Teacher.objects.filter(id=id)
        old_fromdb=Login_tb.objects.filter(id=teacher[0].Loginid.id)
        old_pass=old_fromdb[0].Password
        old=request.POST['old_pass']
        new=request.POST['new_pass']
        if(old==old_pass):
            Login_tb.objects.filter(id=old_fromdb[0].id).update(Password=new)
            messages.success(request,"Password updated")
            return render(request,'common/login.html')
        else:
            messages.error(request,"old password is wrong")
            return render(request,'teacher/changepass.html')
    return render(request,'teacher/changepass.html')