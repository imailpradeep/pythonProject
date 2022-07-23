import pymongo

client = pymongo.MongoClient("mongodb+srv://imailpradeep:ammaacha@cluster0.gujy4jv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Pradeep",
    "email" : "imailpradeep1@gmail.com",
    "surname" : "Bhaskar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
#arfoehfqbpeohfbgqp