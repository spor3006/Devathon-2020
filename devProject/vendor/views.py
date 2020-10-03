from django.shortcuts import render,redirect
from django.http import HttpResponse

import json
import datetime
import time

from django.contrib import auth
from django.core.files import File

from firebase_admin import firestore
import firestoreInitApp
import sys


def viewDashBoard(request):
    return render(request , 'vendor/dashboard.html')




def updateStudentBill(request):
    if request.method == "POST":
        try :
            start_time = time.time()
            posted_data =json.loads(request.body.decode('utf-8'))
            print(posted_data)
            roll_no = posted_data['roll_number']
            items = posted_data['Items']
            quantity = posted_data['qauntity']
            

            db = firestore.client()
            stu_doc = db.collection('Student').where('roll_number','==',roll_no).stream()
            data ={}
            for doc in stu_doc:
                data = doc.to_data()
            
            #update the bill amounts here 


            query_time =  (time.time() - start_time)
            result = {
                'data': data,
                'query_time' : query_time,
                'status' : 'success',
            }
            return HttpResponse(json.dumps(result))
        except : 
            result = {
                'status': 'failed',
                'query_time': query_time,
            }
            return HttpResponse(json.dumps(result))



def getFood(request ):
    if request.method == 'POST':
        try:
            start_time = time.time()
            posted_data =json.loads(request.body.decode('utf-8'))
            print(posted_data)
            day = posted_data['day']
            meal_type = posted_data['meal_type']
            mess = posted_data['mess']

            db= firestore.client()
            doc = db.collection(mess).document(day+"_"+meal_type).get()

            my_dict = doc.to_dict()
            items = []
            price=[]
            items = my_dict.keys()
            price = my_dict.values()

            data_to_send ={
                'items' : items , 
                'price' : price,
            }
            
            query_time =  (time.time() - start_time)
            result = {
                'data': data_to_send,
                'query_time' : query_time,
                'status' : 'success',
            }
            return HttpResponse(json.dumps(result))

        except Exception as e: 
            print(e)
            result = {
                'status': 'failes',
            }
            return HttpResponse(json.dumps(result))

            
