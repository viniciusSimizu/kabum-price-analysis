import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('kabum-price-analysis-25449-firebase-adminsdk-s9ltn-a60bd4706e.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
