from django.urls import path
from Teacher import views

urlpatterns = [
    path('teacherHome',views.teacherHome,name="teacherHome"),
    path('teacher_exam',views.teacher_exam,name="teacher_exam"),
    path('teacher_exam_details',views.teacher_exam_details,name="teacher_exam_details"),
    path('teacher_seating/<int:Hallid>/<int:Dateid>',views.teacher_seating,name="teacher_seating"),
    path('teacher_profile',views.teacher_profile,name="teacher_profile"),
    path('teacher_change',views.teacher_change,name="teacher_change")
]