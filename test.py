from db import (write_data, update_data, 
                check_data, delete_data, 
                check_all_data,
                initialize_client, initialize_collection,
                write_datas, drop_collection) 

from random import randint

import faker

fake = faker.Faker()

def test_initializing():
    from pymongo import MongoClient

    result = initialize_client()

    assert isinstance(result, MongoClient)


def test_initializing_collection():
    from pymongo import database

    result = initialize_collection()

    assert isinstance(result, database.Collection)


def test_writes_data():
    data = {"name": fake.first_name(), "username": "linn", "age": 14}

    result = write_data(data)
    
    assert result['submission_id']

def test_writes_many_data():
    data = list()

    for _ in range(10):
        data.append({"name": fake.first_name(), "username": fake.user_name(), "age": randint(14, 50)})
    
    result = write_datas(data)['submission_ids']

    assert len(result) == 10


def test_check_all_data():
    result = check_all_data()

    assert result

def test_update_data():
    col_data = list(check_all_data())
    data = {"username": fake.user_name()}

    result = update_data({"username": col_data[randint(0, len(col_data))]['username']}, data)

    assert result['modified_count'] == 1


def test_delete_data():
    col_data = list(check_all_data())
    
    result = delete_data({"username": col_data[randint(0, len(col_data))]['username']})

    assert result['deleted_count'] == 1

def test_check_data():
    col_data = list(check_all_data())

    result = check_data({"username": col_data[randint(0, len(col_data))]['username']})

    assert isinstance(result, dict)

def test_drop_collection():
    result = drop_collection()

    assert result == True