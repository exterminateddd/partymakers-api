from pymongo import MongoClient
from utils import get_cfg

db_name = get_cfg()['db_data']['test_db_name']
client = MongoClient(
    'mongodb+srv://main:secret_key@cluster0.zamhd.mongodb.net/'+db_name+'?retryWrites=true&w=majority'
)
data = client[db_name]['parties']
