from django.urls import path
from Student import views

urlpatterns = [
    path('studentHome',views.studentHome,name="studentHome"),
    path('student_exam',views.student_exam,name="student_exam"),
    path('student_profile',views.student_profile,name="student_profile"),
    path('student_change',views.student_change,name="student_change")
]
