from kafka import KafkaProducer
import json
from data import get_registered_user, get_order, get_comment
import time
import random

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer1 = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)
producer2 = KafkaProducer(bootstrap_servers=['localhost:9092'],
                          value_serializer=json_serializer)
producer3 = KafkaProducer(bootstrap_servers=['localhost:9092'],
                          value_serializer=json_serializer)

if __name__ == "__main__":
    while 0 == 0:
        a = random.randint(0, 3)
        if a == 0:
            registered_order = get_order()
            #print(registered_order)
            producer1.send("registered_order", registered_order)
        elif a==1:
            registered_user = get_registered_user()
            #print(registered_user)
            producer2.send("registered_user", registered_user)
        else:
            registered_comment = get_comment()
            #print(registered_comment)
            producer3.send("registered_comment", registered_comment)
        time.sleep(.001)
