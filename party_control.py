from pymongo import MongoClient
from utils import get_cfg

db_name = get_cfg()['db_data']['test_db_name']
client = MongoClient(
    "mongodb+srv://main_exterminated:secret_key@cluster0.tj4ux.gcp.mongodb.net/partymakers_test?retryWrites=true&w=majority"
)
data = client.get_database('partymakers_test').get_collection('parties')


def get_last_id():
    return get_all_parties()[-1]['id']


def create_party(**party_data):
    try:
        insert = data.insert_one({
            "id": get_last_id()+1,
            "name": party_data['name'],
            "desc": party_data['desc'],
            "date": party_data['date'],
            'coordinates': [*party_data['coordinates']],
            'location': {
                'main': party_data['location_main'],
                'add': party_data['location_add'],
            },
            'price': party_data['price'],
            'age': party_data['age']
        })
        if not insert:
            raise Exception('')
    except Exception:
        return False
    return True


def delete_party(name=None, id_=None):
    try:
        if name:
            data.find_one_and_delete({"name": name})
        elif id:
            data.find_one_and_delete({"id": id_})
        else:
            raise Exception
        return True
    except Exception:
        return False


def get_all_parties():
    return [i for i in data.find({})]


def get_party_by_id(id_: int):
    return dict(data.find_one({"id": id_}))
