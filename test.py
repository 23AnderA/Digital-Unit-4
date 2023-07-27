import requests
from api import Datastore

username = 'test'
name = 'bob'
password = '123'
profession = 'clinician'

db = Datastore()
api_test = db.add_staff(username,name,password,profession)

print(api_test)