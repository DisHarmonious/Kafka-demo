-Kafka project with three topics. User registration, Orders and Comments
-The consumers for user registration and orders send the data to an sql database (named "entities")
-The consumer for comments sends the data to a mongo database (named "user_comments)
-Windows Host
-Data generated with faker library

To reproduce this project:
1. Setup Zookeeper and Kafka
2. Create the corresponding databases
3. Start Zookeeper and Kafka
4. Run producer and consumers








