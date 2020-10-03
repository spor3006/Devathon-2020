from django.urls import path,include
from . import views


urlpatterns = [
     path('',views.viewDashBoard),
     path('login',views.Login),
     path('updateStudentBill' , views.updateStudentBill),
     path('getFoodDetails',views.getFood),
]
