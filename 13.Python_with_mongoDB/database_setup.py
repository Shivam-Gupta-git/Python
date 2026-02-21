import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
mongo_url = os.getenv("MONGODB_URL")
client = pymongo.MongoClient(mongo_url, tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db['videos']


print("database connection successfully")