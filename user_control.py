from pymongo import MongoClient
from utils import get_cfg, hs

db_name = get_cfg()['db_data']['test_db_name']
print(db_name)
client = MongoClient(
    "mongodb+srv://main_exterminated:secret_key@cluster0.tj4ux.gcp.mongodb.net/partymakers_test?retryWrites=true&w=majority"
)
data = client.get_database('partymakers_test').get_collection('users')


def username_taken(username: str):
    return True if data.find_one({'username': username}) else False


def register_user(**user_data):
    try:
        insert = data.insert_one({
            'username': user_data['username'],
            'password': hs(user_data['password']),
            'bookmarked': [],
            'data': {
                'firstName': user_data['firstName'],
                'lastName': user_data['lastName']
            }
        })
        if not insert:
            raise Exception('')
    except Exception as e:
        return False
    return True


def check_login(**user_data):
    try:
        find = data.find_one({
            'username': user_data['username'],
            'password': hs(user_data['password'])
        })
        if not find:
            raise Exception('')
    except Exception:
        return False
    return True


def get_all_users():
    return [u for u in data.find({})]


def get_user_data(username: str) -> dict or None:
    return dict(data.find_one({'username': username}))


def get_user_bookmarked_parties(username: str):
    return list(get_user_data(username)['bookmarked'])
