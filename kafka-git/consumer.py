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
        cursor.execute("SELECT COUNT(*) FROM users")
        id_counter=cursor.fetchone()[0]

    #consumer1:
    consumer1=KafkaConsumer("registered_user",
                           bootstrap_servers="localhost:9092",
                           auto_offset_reset='earliest',
                           group_id="group-a")
    print("starting the consumer")
    for msg in consumer1:
        print("Registered User = {}".format(json.loads(msg.value)))
        sql = "INSERT INTO users VALUES (%s, %s, %s, %s, %s)"
        temp = json.loads(msg.value)
        temp2 = list(temp.values())
        id_counter += 1
        temp2 = [id_counter, temp2[0], temp2[1], temp2[2], temp2[3]]
        mycursor.execute(sql, temp2)
        mydb.commit()










