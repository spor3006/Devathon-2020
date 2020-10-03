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
            #print(posted_data)
            roll_no = 123
            items = posted_data['Items']
           
            quantity = posted_data['quantity']
            
            price = posted_data['Selected Price']
            
            total =0

            time1 = time.time()

            current_time = datetime.datetime.now()  

            print(current_time)

            print(time1)
            text =''
            text+= "Date : ---------" + str(current_time) +"\n"

            text+= "Food Item ------- Price ------- quantity    " 
            text+='\n'
            for i in range(0,len(items)):
                total += int(price[i]) * int(quantity[i])
                text += items[i] + "-------" + price[i] + "-------" + quantity[i] 
                text+='\n'

            text+="total ---------- " + str(total)


            print(text)
            print(total)
            

            db = firestore.client()
            stu_doc = db.collection('Student').where('roll_number','==',str(roll_no)).stream()
            data ={}
            for doc in stu_doc:
                data = doc.to_dict()
            
            #update the bill amounts here 
            print(data)
            bill = data['curr_bill']
            bill+=total
            data['curr_bill'] =bill
            transactions = data['transaction_info']
            transactions[str(current_time)] = total 
            data['transaction_info'] = transactions


            db.collection('Student').document(data['id']).set(data)


            query_time =  (time.time() - start_time)
            result = {
                'data': data,
                'query_time' : query_time,
                'status' : 'success',
            }
            return HttpResponse(json.dumps(result))
        except Exception as e : 
            print(e)
            result = {
                'status': 'failed',
                
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
            
            
            for i in my_dict:
                items.append(i)
                price.append(my_dict[i])

            print(items)
            print(price)



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

            
