from kafka import KafkaConsumer
import json
import mysql.connector


if __name__ == "__main__":
    #connect to sql
    sql_check = 1
    if sql_check == 1:
        mydb = mysql.connector.connect(
            host="localhost",
            database="entities",
            user="root",
            password="root"
        )
        mycursor = mydb.cursor()
        print("using entities database")
        cursor=mydb.cursor()
        cursor.execute("SELECT COUNT(*) FROM orders")
        id_counter=cursor.fetchone()[0]
        sql_check=0
    #consumer2
    consumer2 = KafkaConsumer("registered_order",
                            bootstrap_servers = "localhost:9092",
                            auto_offset_reset = 'earliest',
                            group_id = "group-b")
    print("starting the order")
    for msg in consumer2:
        print("Registered Order = {}".format(json.loads(msg.value)))
        sql = "INSERT INTO orders VALUES (%s, %s, %s, %s)"
        temp = json.loads(msg.value)
        temp2 = list(temp.values())
        id_counter += 1
        temp2 = [id_counter, temp2[0], temp2[1], temp2[2]]
        mycursor.execute(sql, temp2)
        mydb.commit()










