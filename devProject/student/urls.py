from django.urls import path,include
from . import views

urlpatterns =[
    path('' , views.Login),
    path('dashboard/<slug:user_id>',views.dashboard),
    path('dashboard/api/getStudentDetails/<slug:roll_no>',views.getStudentData),
    path('dashboard/transactions/api/getStudentDetails/<slug:roll_no>',views.getStudentData),
    path('dashboard/transactions/<slug:user_id>',views.Transactions),
    path('register' , views.Register),

    
]