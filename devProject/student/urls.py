from django.urls import path,include
from . import views

urlpatterns =[
    path('student' , views.Login),
    path('dashboard/<slug:user_id>',views.dashboard),
    path('dashboard/api/getStudentDetails/<slug:roll_no>',views.getStudentData),
    path('Register' , views.Register,name="Register"),
    
]