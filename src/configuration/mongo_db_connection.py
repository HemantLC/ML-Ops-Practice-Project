import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# load the certificate authority file to avoid time-out errors when connecting to MOngoDB
ca = certifi.where()

class MongoDBClient:
    """
    Docstring for MongoDBClient is responsible for establishing a connection to the MongoDB Database
    """
    client = None
    def __init__(self, database_name: str = DATABASE_NAME) -> None:

        try:
            if MongoDBClient.client is None:
                mongo_db_url_key = os.getenv(MONGODB_URL_KEY) # Retrive the URL from environment variables
                if mongo_db_url_key is None:
                    raise Exception(f"Environmrnt variable '{MONGODB_URL_KEY}' is not set")

                # Establish a mongo db client connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url_key, tlsCAFile = ca)

            # Use the shared Mongo client fo rthis instance
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDb connection successful.")

        except Exception as e:
            raise MyException(e,sys)
        