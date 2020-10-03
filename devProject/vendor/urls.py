from django.urls import path,include
from . import views


urlpatterns = [
     path('student',views.viewDashBoard),
     path('vlogin',views.vlogin,name="vloogin"),
     path('updateStudentBill' , views.updateStudentBill),
     path('getFoodDetails',views.getFood),
]