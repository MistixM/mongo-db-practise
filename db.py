from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Constants
DB_URL = "mongodb+srv://mihasik088:D4Mq9cTmsBE3tkd@mongo-learn.glsln.mongodb.net/?retryWrites=true&w=majority&appName=mongo-learn"

def write_data(query: dict) -> dict:
    """
    Write data to the MongoDB collection.

    :query: execute query for the database
    """

    col = initialize_collection()

    try:
        instr = col.insert_one(query)
    except Exception as e:
        return f"Unable to insert data: {e}"
    
    return {"submission_id": instr.inserted_id}

def write_datas(query: dict) -> dict:
    """
    Write multiple data entries to the MongoDB collection.
    """

    col = initialize_collection()

    try:
        result = col.insert_many(query)
    except Exception as e:
        return f"Unable to insert data: {e}"
    
    return {"submission_ids": result.inserted_ids}

def check_data(query: dict) -> dict:
    """
    Check data in the MongoDB collection

    :query: execute query to check for the database
    """

    col = initialize_collection()

    try:
        result = col.find_one(query)
    except Exception as e:
        return f"Unable to retrieve data: {e}"
    
    return result

def check_all_data() -> dict:
    """
    Retrieves all data from the collection
    """
    col = initialize_collection()

    try:
        result = col.find()
    except Exception as e:
        return f"Unable to retrieve all data: {e}"

    return result

def update_data(query: dict, new_data: dict) -> dict:
    """
    Update data in the MongoDB collection

    :query: query to update data
    :new_data: new data to update the existing document with in the database
    """

    col = initialize_collection()

    try:
        result = col.update_one(query, {"$set": new_data})    
    except Exception as e:
        return f"Unable to update data: {e}"

    return {"modified_count": result.modified_count}

def delete_data(query: dict) -> dict:
    """
    Delete data from the MongoDB

    :query: query to delete data from the database
    """

    col = initialize_collection()

    try:
        result = col.delete_one(query)
    except Exception as e:
        return f"Unable to delete data: {e}"
    
    return {"deleted_count": result.deleted_count}

def drop_collection():
    """
    Drops database collection
    """

    col = initialize_collection()

    try:
        col.drop()
    except Exception as e:
        return f"Unable to drop collection: {e}"
    
    return True

def initialize_client() -> object:
    """
    Initializes MongoDB client
    """

    try:
        client = MongoClient(DB_URL, server_api=ServerApi('1'))
    except Exception as e:
        return f"Unable to connect to MongoClient: {e}"
    
    return client

def initialize_collection() -> tuple:
    """
    Initializes MongoDB collection
    """

    client = initialize_client()

    if client:
        db = client['mongo-learn']
        col = db['meetings']

        return col