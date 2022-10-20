from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

print('Animal Shelter Application')
userCreateData = {}       #Input data for write function
userSearchTarget = {}     #Target data for search function
userUpdateFromTarget = {} #Updates data for update function
userUpdateToTarget = {}   #Updates data for update function
userDeleteTarget = {}     #Deletes data for delete function

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, username, password):
        #Initializing the MongoClient. This helps to
        #access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:46639/AAC' % (username, password))
        self.database = self.client['AAC']
        
        
    def obtainCreateData(self):
        #Table to ensure data dict conforms to the expected format
        values = ['1', 'age_upon_outcome', 'animal_type', 'breed', 'color', 'date_of_birth', 'datetime',
                 'monthyear', 'name', 'outcome_subtype', 'outcome_type', 'sex_upon_outcome', 'location_lat',
                 'location_long', 'age_upon_outcome_in_weeks']
        #Loop to obtain input values from user
        for i in range(len(values)):
            key = values[i]
            value = input("Enter " + values[i] + ": ")
            userCreateData.update({key: value})
    
    #Create Method    
    def create(self, data):
        try:
            if data is not None:
                insert_result = self.database.animals.insert_one(data) #Data should be dictionary            
                pprint(insert_result)
                return True #Return value for boolean requirement
            else:
                raise Exception("Nothing to save, because data is empty")
        except:
            return False #Return value for boolean requirement
    
    #Obtain Read data
    def obtainReadData(self):
        for i in range(1):
            key = input("Enter search key: ")
            value = input("Enter search value: ")
            userSearchTarget.update({key: value})
            
    #Read Method    
    def read(self, data):
        try:
            if data is not None:
                read_result = list(self.database.animals.find(data, {"_id":False})) #Data should be dictionary 
                return read_result
            else:
                raise Exception("Nothing to return, because data parameter is empty")
                return False
        except Exception as e:
            print("An exception occured: ", e)
            
    #Obtain Update data
    def ObtainUpdateData(self):
        for i in range(1):
            key = input("Enter update key: ")
            value = input("Enter update value: ")
        userUpdateFromTarget.update({key: value})
        #Obtain ne data to change the target to
        for i in range(1):
            key = input("Enter update key: ")
            value = input("Enter new update value: ")
        userUpdateToTarget.update({'$set': {key: value}})
        print(userUpdateToTarget)
        
    
    #Update Method
    def update(self, fromTarget, toTarget, count):
        if fromTarget is not None:
            if count == 1:
                update_result = self.database.animals.update_one(fromTarget, toTarget)
                pprint("Matched Count: " + str(update_result.matched_count) + ", Modified Count: " + str(update_result.modified_count))
                if update_result.modified_count == 1:
                    print("Success!")
                    print(update_result)
                    return True
                else:
                    print("Something went wrong")
                    return False
            elif count == 2:
                update_result = self.database.animals.update_many(fromTarget, toTarget)
                pprint("Matched Count: " + str(update_result.matched_count) + ", Modified Count: " + str(update_result.modified_count))
                if update_result.modified_count == update_result.matched_count:
                    print("Success!")
                    print(update_result)
                    return True
                else:
                    print("Something went wrong, all items matching the target may not have been updated. Run a search to verify")
                    print(update_result)
                    return True
            else:
                print("Count not recognized. Try again.")
                return False
        else:
            #Let the user know there is a problem
            raise Exception("Nothing to update, because at least one of the target parameters is empty")
            return False
    
    #Obtain data for delete method
    def obtainDeleteData(self):
        for i in range(1):
            key = input("Enter delete key: ")
            value = input("Enter delete value: ")
            userDeleteTarget.update({key: value})
    
    #Delete Method
    def delete(self, target, count):
        if data is not None:
            if count == 1:
                try:
                    delete_result = self.database.animals.delete_one(Target)
                    pprint("Deleted Count: " + str(delete_result.deleted_count))
                    if delete_result.delete_count == 0:
                        print("Nothing to be deleted using the target data.")
                        print(delete_result)
                        return True
                    else:
                        print("Success!")
                        print(delete_result)
                        return True
                except Exception as e:
                    print("An exception has occured: ", e)
                    return False
            else:
                print("Count not recognized. Try again.")
                return False
        else:
            raise Exception("Nothing to delete, because the target parameter is empty")
            return False
                    