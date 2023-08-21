import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username, password):
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32168
        DB   = "AAC"
        COL  = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    def create(self, data):
        # Function to create a document
        # Conditional statement to check if data variable is empty
        if data is not None:
            # When true, mongo class member function inserts data in collection
            self.collection.insert_one(data)
            # Boolean value returned after execution
            return True
        else:
            # Exception and output when user enters a None parameter
            raise Exception("Nothing to save, because data parameter is empty")
            # Boolean value returned after execution
            return False
            
    def read(self, data):
        # Function to read a document or multiple documents
        # Declare list
        docs = []
        if data is not None:
            # Declare and assign variable to cursor object
            result = self.collection.find(data)
            # Cast cursor object as a list and return to function call
            return list(result)
        else:
            # When data is empty, the method returns an empty list
            return docs

    def update(self, searchData, newData):
        # Function to read a document or multiple documents
        # Conditional statement to check if data variable is empty
        if searchData is not None:
            # Declare and assign variable to number of updated documents
            result = self.collection.update_one(searchData, {"$set": newData})
            # Return matched count to function call
            return result.matched_count
        else:
            # When the searchData is None
            raise Exception("There was not a match to update")

    def delete(self, data):
        # Function to read a document or multiple documents
        # Conditional statement to check if data variable is empty
        if data is not None:
            # Declare and assign variable to number of updated documents
            result = self.collection.delete_one(data)
            # Return deleted count to function call
            return result.deleted_count
        else:
            raise Exception("There was not a match to delete")
