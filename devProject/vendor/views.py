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
            bill_amt = posted_data['Net Amount']

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

