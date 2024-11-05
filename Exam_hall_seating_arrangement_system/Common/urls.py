from django.urls import path
from Common import views
urlpatterns = [
    path('',views.index,name=''),
    path('login/',views.login,name='login'),
    path('logout_handler',views.logout_handler,name="logout_handler"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('reset-password/<str:token>/', views.reset_password_view, name='reset_password'),
]
