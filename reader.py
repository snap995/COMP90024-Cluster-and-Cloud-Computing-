import json
import pandas as pd
import couchdb
data=[]
ckey = ""
csecret = ""
atoken = ""
asecret = ""
couch = couchdb.Server('http://couchdbadmin:vinayaka@45.113.235.12:5984')
db = couch['tweetsdb']

cred = db["credentials"]

ckey = cred["ckey"]
csecret = cred["csecret"]
atoken = cred["atoken"]
asecret = cred["asecret"]
doc_id = 'tweets'
if doc_id in db:
	doc = db[doc_id]
else:
	db[doc_id] = {}
	doc = db[doc_id]
	
with open('smallTwitter.json' , 'r',encoding = "utf-8") as f:
	for x in f:
		data.append(x)
		
data.pop(0)
print(data[0])

for y in data:
	id = y.split('"id":"')[1].split('","key"')[0]
	date = y.split(',"created_at":"')[1].split('","text"')[0]
	text = y.split(',"text":"')[1].split('","location"')[0]
	print(id)
	print(date)
	print(text)
	try:
			doc[id] = [date , text]
			db.save(doc)
			print('ran')
	except BaseException as e:
			print('reached the end')