from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse




def adminhome(request):
    return render(request,'admin/adminhome.html')
def add_course(request):
    if request.method == "POST":
        course=request.POST['course']
        if(Course.objects.filter(course__iexact=course).exists()):
            messages.error(request,"Course name already exist")
            return render(request,'admin/add_dep.html')
        else:
            data=Course(course=course)
            data.save()
            return redirect(view_course)      
    return render(request,'admin/add_dep.html')

def view_course(request):
    cour=Course.objects.all()
    p=Paginator(cour,2)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    return render(request,'admin/view_dep.html',{'course':page_obj})
def edit_course(request,id):
    if request.method == "POST":
        depa=request.POST['course']
        Course.objects.filter(id=id).update(course=depa)
        messages.success(request,'Updated')
        return redirect(view_course)

    dep=Course.objects.filter(id=id)
    return render(request,'admin/add_dep.html',{'de':dep})


def delete_course(request,id):
    Course.objects.filter(id=id).delete()
    messages.success(request,'Deleted')
    return redirect(view_course)
def add_subject(request):
    depa=Course.objects.all()
    if request.method == "POST":
        dep=request.POST['course']
        sub=request.POST['subject']
        data=Subject(courseid_id=dep,subject=sub)
        data.save()
        messages.success(request,'Added..')
        return redirect(view_subject)
    return render(request,'admin/add_subject.html',{'de':depa})
def view_subject(request):
    sub=Subject.objects.all()
    p=Paginator(sub,5)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    return render(request,'admin/view_subject.html',{'subject':page_obj})
def edit_subject(request,id):
    if request.method == "POST":
        sub=request.POST['subject']
        course=request.POST['course']
        Subject.objects.filter(id=id).update(courseid_id=course,subject=sub)
        messages.success(request,"updated...")
        return redirect(view_subject)
    subject=Subject.objects.filter(id=id)
    course=Course.objects.all()
    return render(request,'admin/add_subject.html',{'sub':subject,'co':course})

def subject_del(request,id):
    Subject.objects.filter(id=id).delete()
    messages.success(request,'Deleted..')
    return redirect(view_subject)


def get_sub(request):
    d_id=request.GET['id']
    subje=Subject.objects.filter(courseid=d_id)
    return render(request,'admin/getsub.html',{'su':subje})

def add_staff(request):
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        gender=request.POST['gender']
        sub=request.POST['subject']
        contact=request.POST['contact']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        
        login=Login_tb(Username=username,Password=password,User_type="Teacher")
        login.save()
        teacher=Teacher(First_name=fname,Last_name=lname,Gender=gender,Subjectid_id=sub,Contact=contact,Email=email,Loginid_id=login.id)
        teacher.save()
        messages.success(request,'Registration was succesfull')
        return redirect(staff_management)
    depa=Course.objects.all()
    return render(request,'admin/add_staff.html',{'de':depa})

def manage_student(request):
    student=Student.objects.all()
    paging=Paginator(student,3)
    page_number=request.GET.get('page')
    page_obj=paging.get_page(page_number)
    return render(request,'admin/manage_student.html',{'st':page_obj})


def staff_management(request):
    staff=Teacher.objects.all()
    paging=Paginator(staff,2)
    page_number=request.GET.get('page')
    page_obj=paging.get_page(page_number)
    return render(request,'admin/staff_management.html',{'staff':page_obj})

def edit_staff(request,id):
    if request.method == "POST":
        data=get_object_or_404(Teacher,id=id)
        fname=request.POST['fname']
        lname=request.POST['lname']
        gender=request.POST['gender']
        sub=request.POST['subject']
        contact=request.POST['contact']
        email=request.POST['email']
        username=request.POST['username']
        Teacher.objects.filter(id=id).update(First_name=fname,Last_name=lname,Gender=gender,Subjectid_id=sub,Contact=contact,Email=email)
        Login_tb.objects.filter(id=data.Loginid_id).update(Username=username)
        messages.success(request,'Updated..')
        return redirect(staff_management)

    course=Course.objects.all()
    staff=Teacher.objects.filter(id=id)
    return render(request,'admin/edit_staff.html',{'st':staff,'co':course})

def delete_staff(request,id):
    teacher=Teacher.objects.filter(id=id)
    Login_tb.objects.filter(id=teacher[0].Loginid.id).delete()
    teacher.delete()
    return redirect(staff_management)

def add_student(request):
    course=Course.objects.all()
    if request.method =="POST":
        number=request.POST['register']
        fname=request.POST['fname']
        lname=request.POST['lname']
        course=request.POST['course']
        depar=request.POST['department']
        semester=request.POST['semester']
        if len(request.FILES)>0:
            img=request.FILES['image']
        else:
            img="No Image"
        username=request.POST['username']
        mail=request.POST['mailid']
        mobile=request.POST['mobile']
        address=request.POST['address']
        password=request.POST['password']
        login=Login_tb(Username=username,Password=password,User_type="Student")
        login.save()
        student=Student(Register_number=number,First_name=fname,Last_name=lname,course_id=course,Department=depar,Semester=semester,Image=img,Mobile=mobile,Address=address,Email=mail,Loginid_id=login.id)
        student.save()

        
        return redirect(manage_student)
    
    return render(request,'admin/add_student.html',{'co':course})

def get_details(request):
    id=request.GET['st']
    student=Student.objects.filter(id=id)
    return render(request,'admin/partial_student.html',{'stu':student})

def edit_student(request,id):
    if request.method == "POST":
        student=Student.objects.filter(id=id)
        number=request.POST['register']
        fname=request.POST['fname']
        lname=request.POST['lname']
        course=request.POST['course']
        depar=request.POST['department']
        semester=request.POST['semester']
        if len(request.FILES)>0:
            img=request.FILES['image']
        else:
            img=student[0].Image
        username=request.POST['username']
        mail=request.POST['mailid']
        mobile=request.POST['mobile']
        address=request.POST['address']
        student.update(Register_number=number,First_name=fname,Last_name=lname,course_id=course,Department=depar,Semester=semester,Mobile=mobile,Address=address,Email=mail)
        Login_tb.objects.filter(id=student[0].Loginid_id).update(Username=username)
        imag_obj=Student.objects.get(id=id)
        imag_obj.Image=img
        imag_obj.save()
        return redirect(manage_student)
    else:
        course=Course.objects.all()
        student=Student.objects.filter(id=id)
        return render(request,'admin/add_student.html',{'st':student,'co':course})

def delete_student(request,id):
    student=Student.objects.filter(id=id)
    Login_tb.objects.filter(id=student[0].Loginid.id).delete()
    student.delete()
    messages.success(request,'record deleted..')
    return redirect(manage_student)

def hall_management(request):
    hall=Hall.objects.all()
    return render(request,'admin/hall_management.html',{'ha':hall})

def add_hall(request):
    if request.method == "POST":
        no=request.POST['hall_no']
        capacity=request.POST['capacity']
        data=Hall(Hall_no=no,Capacity=capacity)
        data.save()
        return redirect(hall_management)
    return render(request,'admin/add_hall.html')

def hall_edit(request,id):
    if request.method == "POST":
        no=request.POST['hall_no']
        capacity=request.POST['capacity']
        Hall.objects.filter(id=id).update(Hall_no=no,Capacity=capacity)
        return redirect(hall_management)
    hall=Hall.objects.filter(id=id)
    return render(request,'admin/add_hall.html',{'ha':hall})

def hall_delete(request,id):
    Hall.objects.filter(id=id).delete()
    return redirect(hall_management)

def exam_management(request):
    exam=Exam.objects.all()
    p=Paginator(exam,2)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    return render(request,'admin/exam_management.html',{'ex':page_obj})

def getExam_date(request):
    if 'search_date' in request.GET:
        search_date = request.GET['search_date']  # Get the date input from the search bar
        try:
            # Find the date object matching the input date
            date_obj = Exam_date.objects.get(Date_of_exam=search_date)
            exams = Exam.objects.filter(Date=date_obj)
            return render(request, 'admin/exam_management.html', {
                'ex': exams,
                'search_date': search_date
            })
        except Exam_date.DoesNotExist:
            # Handle the case where the date doesn't exist in the database
            return render(request, 'admin/exam_management.html', {
                'error': 'No seating arrangements found for the selected date.'
            })
    else:
        return render(request, 'admin/exam_management.html')

def add_exam(request):
    cou=Course.objects.all()
    if request.method == "POST":
        subject=request.POST['subject']
        date=request.POST['Date']
        time=request.POST['time']
        duration=request.POST['duration']
        semester=request.POST['semester']
        if(Exam_date.objects.filter(Date_of_exam=date)):
            examid=Exam_date.objects.filter(Date_of_exam=date).values("id")
            data=Exam(subject_id=subject,Date_id=examid,Time=time,Duration=duration,Semester=semester)
        else:
            exam=Exam_date(Date_of_exam=date)
            exam.save()
            data=Exam(subject_id=subject,Date_id=exam.id,Time=time,Duration=duration,Semester=semester)

        data.save()
        return redirect(exam_management)

    return render(request,'admin/add_exam.html',{'co':cou})

def edit_exam(request,id):
    cou=Course.objects.all()
    if request.method == "POST":
        subject=request.POST['subject']
        date=request.POST['Date']
        time=request.POST['time']
        duration=request.POST['duration']
        semester=request.POST['semester']
        old_exam=Exam.objects.filter(id=id)
        Exam_date.objects.filter(id=old_exam[0].Date_id).update(Date_of_exam=date)
        old_exam.update(subject_id=subject,Time=time,Duration=duration,Semester=semester)
        return redirect(exam_management)
    else:
         
        exam=Exam.objects.filter(id=id)
        start_time = exam[0].Time.strftime('%H:%M')
        return render(request,'admin/add_exam.html',{'ex':exam,'co':cou,'time':start_time})
    
def delete_exam(request,id):
    exam=Exam.objects.filter(id=id).delete()
    return redirect(exam_management)
def allocation(request):
    if request.method == "POST":
        date=request.POST['Date']
        date_obj=Exam_date.objects.filter(Date_of_exam=date)
        date_id=date_obj[0].id
        subjectid=request.POST.getlist('subject')
        subject_ids = ','.join(subjectid)
        shift=request.POST['shift']
        name=request.POST['name']
        hall=request.POST['hall']
        data=Allocation(Date_id=date_id,Subject_ids=subject_ids,Shift=shift,Invigilator_name_id=name,Hallid_id=hall)
        data.save()
    Invigilator_name=Teacher.objects.all()
    hall_no=Hall.objects.all()
    return render(request,'admin/allocation.html',{'inv':Invigilator_name,'ha':hall_no})
def allo_sub(request):
    date=request.GET['da']
    date_id=Exam_date.objects.filter(Date_of_exam=date)
    subje=Exam.objects.filter(Date=date_id[0].id)
    return render(request,'admin/getsub.html',{'exam':subje})
  


def seating(request):
    if request.method == "POST":
        ex=request.POST['date']
        ha=request.POST['hall']
        stu=request.POST['student']
        seat=request.POST['seat_number']
        hall=Hall.objects.filter(id=ha)
        capacity=hall[0].Capacity
        if(int(seat)<=capacity):
            data=Seating_Arrangement(examid_id=ex,hallid_id=ha,studentid_id=stu,seat_no=seat)
            data.save()
            return redirect(view_seating)
        else:
            messages.error(request,"Out Of capacity,please select another hall")
            return redirect(view_seating)
    else:    
        hall=Hall.objects.all()
        student=Student.objects.all()
        exam = Exam_date.objects.all()  
        return render(request,'admin/seating.html',{'ha':hall,'st':student,'ex':exam})


def get_next_seat_number(request, hall_id,dateId):
    try:
        #Get the selected hall
        hall = Hall.objects.get(id=hall_id)
        
        #Count how many seats are already assigned for this hall
        assigned_seats = Seating_Arrangement.objects.filter(hallid=hall,examid=dateId).count()
        
        # Check if the hall has available seats
        if assigned_seats < hall.Capacity:
            next_seat_number = assigned_seats + 1  # Assign next available seat number
        else:
            next_seat_number = 'Full'  # Hall is full

        return JsonResponse({'next_seat_number': next_seat_number})

    except Hall.DoesNotExist:
        return JsonResponse({'error': 'Hall not found'}, status=404)

def view_seating(request):
    seating=Seating_Arrangement.objects.all()
    paging=Paginator(seating,6)
    number=request.GET.get('page')
    page_obj=paging.get_page(number)    
    return render(request,'admin/view_seating.html',{'seat':page_obj})


def search_seating(request):
    if 'search_date' in request.GET:
        search_date = request.GET['search_date']  # Get the date input from the search bar

        try:
            # Find the date object matching the input date
            date_obj = Exam_date.objects.get(Date_of_exam=search_date)

            # Query the seating arrangement using the date ID
            seating_arrangements = Seating_Arrangement.objects.filter(examid=date_obj)

            return render(request, 'admin/view_seating.html', {
                'seat': seating_arrangements,
                'search_date': search_date
            })
        except Exam_date.DoesNotExist:
            # Handle the case where the date doesn't exist in the database
            return render(request, 'admin/view_seating.html', {
                'error': 'No seating arrangements found for the selected date.'
            })
    else:
        return render(request, 'admin/view_seating.html')


def seating_edit(request,id):
    if request.method == "POST":
        ex=request.POST['date']
        ha=request.POST['hall']
        stu=request.POST['student']
        seat=request.POST['seat_number']
        hall=Hall.objects.filter(id=ha)
        capacity=hall[0].Capacity
        if(int(seat)<=capacity):
            Seating_Arrangement.objects.filter(id=id).update(examid_id=ex,hallid_id=ha,studentid_id=stu,seat_no=seat)
            return redirect(view_seating)
        else:
            messages.error(request,"Out Of capacity,please select another hall")
            return redirect(view_seating)
    data=Seating_Arrangement.objects.filter(id=id)
    hall=Hall.objects.all()
    student=Student.objects.all()
    exam = Exam_date.objects.all() 
    return render(request,'admin/seating.html',{'da':data,'ha':hall,'st':student,'ex':exam})

def view_allocation(request):
    allocations = Allocation.objects.all()
    for allocation in allocations:
        subject_ids = allocation.Subject_ids.split(',')
        subjects = Subject.objects.filter(id__in=subject_ids)
        allocation.Subject_ids = [subject.subject for subject in subjects]

    p=Paginator(allocations,2)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    return render(request, 'admin/view_allocation.html', {'all': page_obj})


def allocation_edit(request,id):
    if request.method == "POST":
        shift=request.POST['shift']
        invigi_name=request.POST['name']
        hall_name=request.POST['hall']
        Allocation.objects.filter(id=id).update(Shift=shift,Invigilator_name=invigi_name,Hallid_id=hall_name)
        return redirect(view_allocation)
    else:
        hall_no=Hall.objects.all()
        invigilator=Teacher.objects.all()
        data=Allocation.objects.filter(id=id).first()

        if data:
            subject_ids = data.Subject_ids.split(',')
            subjects = Subject.objects.filter(id__in=subject_ids)
            subject_names = ', '.join([subject.subject for subject in subjects])

            context = {
                'inv': invigilator,
                'ha':hall_no,
                'all':data,
                'subject':subject_names
            }
            return render(request, 'admin/allocation_edit.html', context)
        else:
            return redirect(view_allocation)
    
