from django.urls import path
from Site_admin import views

urlpatterns = [
    path('adminhome',views.adminhome,name="adminhome"),
    path('add_course',views.add_course,name="add_course"),
    path('view_course',views.view_course,name="view_course"),
    path('edit_course/<int:id>',views.edit_course,name="edit_course"),
    path('delete_course/<int:id>',views.delete_course,name="delete_course"),
    path('add_subject',views.add_subject,name="add_subject"),
    path('view_subject',views.view_subject,name="view_subject"),
    path('edit_subject/<int:id>',views.edit_subject,name="edit_subject"),
    path('subject_del/<int:id>',views.subject_del,name="subject_del"),
    path('staff_management',views.staff_management,name="staff_management"),
    path('add_staff',views.add_staff,name="add_staff"),
    path('edit_staff/<int:id>',views.edit_staff,name="edit_staff"),
    path('delete_staff/<int:id>',views.delete_staff,name="delete_staff"),
    path('get_sub',views.get_sub,name="get_sub"),
    path('manage_student',views.manage_student,name="manage_student"),
    path('get_details',views.get_details,name="get_details"),
    path('add_student',views.add_student,name="add_student"),
    path('edit_student/<int:id>',views.edit_student,name="edit_student"),
    path('delete_student/<int:id>',views.delete_student,name="delete_student"),
    path('hall_management',views.hall_management,name="hall_management"),
    path('add_hall',views.add_hall,name="add_hall"),
    path('hall_edit/<int:id>',views.hall_edit,name="hall_edit"),
    path('hall_delete/<int:id>',views.hall_delete,name="hall_delete"),
    path('exam_management',views.exam_management,name="exam_management"),
    path('add_exam',views.add_exam,name="add_exam"),
    path('getExam_date',views.getExam_date,name="getExam_date"),
    path('edit_exam/<int:id>',views.edit_exam,name="edit_exam"),
    path('seating/get-next-seat-number/<int:hall_id>/<int:dateId>/', views.get_next_seat_number, name='get_next_seat_number'),
    path('seating/',views.seating,name="seating"),
    path('view_seating',views.view_seating,name="view_seating"),
    path('search_seating/', views.search_seating, name='search_seating'),
    path('seating_edit/<int:id>',views.seating_edit,name="seating_edit"),
    path('delete_exam/<int:id>',views.delete_exam,name="delete_exam"),
    path('allocation',views.allocation,name="allocation"),
    path('allo_sub',views.allo_sub,name="allo_sub"),
    path('view_allocation',views.view_allocation,name="view_allocation"),
    path('allocation_edit/<int:id>',views.allocation_edit,name="allocation_edit"),
    
]

