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
# Create your views here.
def Register(request):
    if request == "POST":
        roll_number = request.POST['roll_no']
        fname= request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        student_info ={}

        student_info['roll_number'] = roll_number
        student_info['fname']=fname
        student_info['lname'] = lname
        student_info['email'] = email
        student_info['username'] = username
        student_info['password'] = password

        student_info['transaction_info'] ={}
        student_info['curr_bill'] = 0
        try:
            db = firestore.client()

            doc = db.collection('Student').document()
            student_info['id'] = doc.id
            doc.set(student_info)

        except: 
            print("Failed to Reach Database")

def Login(request):
    if request.method == 'POST' :

        data = json.loads(request.body.decode('utf-8'))
        print(data)
        username = data['username']
        
        password = data['password']
        
        try:
            db = firestore.client()
            existing = db.collection('Student').where("username" ,'==',username).stream()
            if(len(list(existing))>0):
                #print(existing)
                existing2 = db.collection('Student').where("username" ,'==',username).stream()
                #print(existing2)
                for my_doc in existing2 :
                    #print("This")
                    #print(my_doc)
                    my_dict = my_doc.to_dict()
                    print(my_dict)
                    passW = my_dict['password']
                    student_id = my_dict['id']
                    if(password==passW):
                        #print("here2")
                        response = {'status': 'success','url': 'student/dashboard/'+student_id,}
                        #print(response)
                        #print("This")
                        response = json.dumps(response)
                        return HttpResponse(response)
                    else:

                        response = {'status' : 'fail','message' : 'Invalid Credentials'}
                        print("Not This")
                        response = json.dumps(response)
                        return HttpResponse(response)

        
            else :
                response = {'status' : 'fail','message' : 'Unable to Reach data base'}
                print("Not This")
                response = json.dumps(response)
                return HttpResponse(response)
        except:
            return HttpResponse("Unable to Fetch Data")
    if request.method == "GET" :
        return redirect('/login')

def index(request):
        return render(request , 'student/dashboard.html')


def dashboard(request , user_id):
    return render(request , 'student/dashboard.html' , {'user_id': user_id} )

def getStudentData(request,roll_no):
    try:
        print("Fetching Data")
        start_time = time.time()
        db = firestore.client()
        stu_doc = db.collection("Student").where('roll_number','==',roll_no).stream()
        student_data = {}
        for doc in stu_doc:
            student_data = doc.to_dict()
        
        print(student_data)

        query_time =  (time.time() - start_time)
        result = {
            'status': 'success',
            'query_time': query_time,
            'data': student_data
        }
        return HttpResponse(json.dumps(result))

        
    except: 
        print("errors")

