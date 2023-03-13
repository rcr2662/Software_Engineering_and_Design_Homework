from pymongo import MongoClient 
from datetime import datetime

#Connect to cluster on MongoDB
Client=MongoClient("mongodb+srv://asamant:MApeZZu5VcMpD6t3@cluster0.oovet.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 
#Get database
db = Client.HW4Fall22
#Create collection in database
collection = db["rcr2662"]

datetime = datetime.now()
#Document with fields to be added
information = {
    "Name" : "Roberto Reyes",
    "Creation_Date" : datetime,
    "Programming_Languages" : ["Python", "Java", "C"],
    "Number_of_Projects": 5
}

#Insert document to collection
collection.insert_one(information)

#Close connection to cluster
Client.close()
