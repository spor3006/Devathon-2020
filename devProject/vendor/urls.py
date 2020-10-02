from django.urls import path,include
from . import views


urlpatterns = [
     path('',views.viewDashBoard),
     path('updateStudentBill' , views.updateStudentBill)
]
