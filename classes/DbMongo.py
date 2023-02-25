import pymongo
import os
from dotenv import load_dotenv

class DBMongo:
    
    
    @staticmethod
    def getDB():
        load_dotenv()
        user = os.environ['USERDB']
        password = os.environ['PASSWORDDB']
        cluster = os.environ['CLUSTER']
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )
 
        client = pymongo.MongoClient(uri)
        db = client[os.environ['DB']]

        return client, db
    

    
       