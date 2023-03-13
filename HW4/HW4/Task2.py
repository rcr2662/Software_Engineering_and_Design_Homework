from pymongo import MongoClient 

#Connect to cluster
Client=MongoClient("mongodb+srv://rcr2662:rcr2662@cluster0.qamikah.mongodb.net/?retryWrites=true&w=majority")
#Get database
db = Client.HW4

#create collections
collection1 = db["Collection1: HW Set"]
collection2 = db["Collection2: Projects"]

#Document for collection1
document1 = {
    "Name" : "HWSet1",
    "Capacity" : 200,
    "Availability" : 100
}

#Insert document into collection1
collection1.insert_one(document1)

#Document for collection2
document1 = {
    "Name" : "Project1",
    "ID" : "as1234", 
    "Description" : "This is the first project" 
}

#Insert document into collection2
collection2.insert_one(document1)

#Close connection to cluster
Client.close()