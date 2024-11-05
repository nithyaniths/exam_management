from django.shortcuts import render,redirect
from django.contrib.auth import logout
from Site_admin.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils.html import format_html
from django.shortcuts import render, redirect, get_object_or_404
from .models import PasswordResetToken


def index(request):
    if request.session.get('Role') == 'Admin':
        return render(request,'admin/adminhome.html')
    elif request.session.get('Role') == 'Student':
        return render(request,'student/home.html')
    elif request.session.get('Role') == 'Teacher':
        return render(request,'teacher/home.html')
    return render(request,'common/login.html')

def login(request):    
    username=request.POST['username']
    password=request.POST['password']
    admin=Admin_tb.objects.filter(username=username,password=password)
    student=Login_tb.objects.filter(Username=username,Password=password,User_type="Student")
    teacher=Login_tb.objects.filter(Username=username,Password=password,User_type="Teacher")
    if admin.count()>0:
        request.session['adminid']=admin[0].id
        request.session["Role"]="Admin"
        return redirect('adminhome')
    elif student.count()>0:
        stu=Student.objects.filter(Loginid=student[0].id)
        request.session['studentid']=stu[0].id
        request.session['username']=stu[0].Loginid.Username
        request.session["Role"]="Student"
        return redirect('studentHome')
    elif teacher.count()>0:
        tea=Teacher.objects.filter(Loginid=teacher[0].id)
        print(tea)
        request.session['teacherid']=tea[0].id
        request.session['username']=tea[0].Loginid.Username
        request.session["Role"]="Teacher"
        return redirect('teacherHome')
    else:
        messages.info(request,"login failed")
        return render(request,'common/login.html')


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']        
        # Generate a random token
        token = get_random_string(length=32)
        
        # Save the token in the database
        reset_token = PasswordResetToken.objects.create(Email=email, token=token)
        
        # Construct the reset URL (you can change domain as needed)
        reset_url = request.build_absolute_uri(f'/reset-password/{token}/')
        message_html = format_html(
        '<p>Click the link below to reset your password:</p>'
        '<p><a href="{}">Reset Password</a></p>',
        reset_url
        )

        message_plain = f'Click the link below to reset your password:\n{reset_url}'
        # Send an email with the reset URL
        send_mail(
            'Password Reset Request',
            message_plain,
            'rosmicheriyan@gmail.com',  # from email
            [email],  # recipient
            fail_silently=False,
            html_message=message_html
        )
        
        return render(request, 'common/password_reset_sent.html')
    
    return render(request, 'common/forgotpassword.html')

def reset_password_view(request, token):  
    reset_token = get_object_or_404(PasswordResetToken, token=token)
    print(reset_token)
    print(reset_token.Email)
    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if new_password and new_password == confirm_password:
            #Assuming you're resetting password for the Teacher model
            teacher = Teacher.objects.filter(Email=reset_token.Email).first()
            
            student = Student.objects.filter(Email=reset_token.Email).first()
           
            if teacher:
                teacher.Loginid.Password =new_password
                teacher.Loginid.save()
                # Delete the token after successful reset
                
            elif student:
                student.Loginid.Password =new_password
                student.Loginid.save()
                # Delete the token after successful reset
            else:
                return render(request, 'common/forgotpassword.html')
            reset_token.delete()
            return redirect(index)
        else:
            # Handle password mismatch or empty password case
            return render(request, 'common/reset_password.html', {'error': 'Passwords do not match!'})

    return render(request, 'common/reset_password.html', {'token': token}) 

def logout_handler(request):
    logout(request)
    request.session.flush()
    return redirect(index)