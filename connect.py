import os
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "firebasecloudassignment-firebase-adminsdk-credentials.json"	#this json is confidential and isn't included in git

def connect():	#this function returns a db object after connecting with given credentials. we should only ever run it once per session.
	cred = credentials.ApplicationDefault()
	firebase_admin.initialize_app(cred, {'projectId': 'firebasecloudassignment'})	#initialize a connection to our project
	db = firestore.client()
	return db

def test_connection():
	db = connect()
	if db:	#if we get anything back, we've probably connected.
		print("Connection successful.")
		return db	#this db should be passed around to every other function as needed.
	else:	#otherwise, inform the user
		print("Error! Not connected! Recheck credentials and try again.")

def add_name(db, name_dict):
	location = 'name_' + name_dict['lastname']	#each entry has a unique document, consisting of 'name_' and the last name.
	test_reference = db.collection(u'names').document(location)	#we tell the db where we're putting data...
	test_reference.set({	#and proceed to set it.
		u'firstname': name_dict['firstname'],
		u'lastname': name_dict['lastname']
		})

def read_names(db):
	names_collection = db.collection(u'names')
	stream = names_collection.stream()	#obtain stream object from our aforedefined collection
	for x in stream:	#...and iterate over it.
		print(f'{x.id} => {x.to_dict()}')