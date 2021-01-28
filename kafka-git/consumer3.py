from kafka import KafkaConsumer
import json
import pymongo

if __name__ == "__main__":
    #Connect to Mongo
    mongo_check = 1
    if mongo_check == 1:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["user_comments"]
        col = db["comments"]
        '''
        mydict = { "name": "John", "address": "Highway 37" }
        x = mycol.insert_one(mydict)
        '''
        mongo_check=0
        print("connected to mongo")
    #consumer3
    consumer3 = KafkaConsumer("registered_comment",
                            bootstrap_servers="localhost:9092",
                            auto_offset_reset='earliest',
                            group_id="group-c")
    print("starting the comment")
    for msg in consumer3:
        print("Registered comment = {}".format(json.loads(msg.value)))
        col.insert_one(json.loads(msg.value))







