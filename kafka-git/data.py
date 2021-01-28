from faker import Faker
import random

fake=Faker()

def get_registered_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "country": fake.country(),
        "date": fake.date()
    }

def get_order():
    return{
        "item": fake.word(),
        "quantity": fake.year(),
        "date": fake.date()
    }

def get_comment():
    return{
        "text": fake.text(),
        "date": fake.date(),
        "name": fake.name(),
        "country": fake.country()
    }

if __name__=="__main__":
    print(get_registered_user())
    print(get_order())
    print(get_comment())


















