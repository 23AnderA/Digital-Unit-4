import requests
from api import Datastore

username = 'bahlin1'

db = Datastore()
api_test = db.get_password(username)

print(api_test)