import json


from firebase_admin import firestore
import firestoreInitApp


def testRun():
    try:
        db = firestore.client()
        docs = db.collection('Student').stream()
        collection_doc = db.collection('Student').document()
        student_info = {}
        student_info['roll'] = 1234
        student_info['id'] = collection_doc.id
        student_info['transaction_details'] = {"Hello" : 123}

        collection_doc.set(student_info)
        for doc in docs:
            #doc_ref = doc.collection('TransactionDetails').get()
           # student_details = doc_ref.to_dict()
            print(doc.id)
            #id = doc.id
            

    except :
        print("Its Ok! You have to face Errors")

#estRun()


def setMess():
    try :
        db = firestore.client()
        coll = db.collection('Mess_1')

        days = ['Monday' , 'Tuesday' , 'Wednesday ' , 'Thursday' , 'Friday']
        meals = ['Breakfast' , 'Lunch' , 'Snacks'  , 'Dinner']

        for day in days:
            for meal in meals:
                doc_name = day+"_"+meal
                doc = coll.document(doc_name)
                data={}
                doc.set(data)
                print(doc_name)

    except:
        print("Could not reach the database")


setMess()