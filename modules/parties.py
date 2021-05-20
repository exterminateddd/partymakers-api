from flask import Blueprint, request, session, jsonify

from party_control import *


blueprint = Blueprint("auth", __name__)


@blueprint.route('/party/create_party', methods=['POST'])
def create_party_route():
    json_ = request.get_json(force=True)
    resp = {
        'success': True,
        'msg': 'Successfully created party.',
        'data': {}
    }
    try:
        for k in ['name', 'desc', 'date', 'coordinates', 'location_main', 'location_add', 'price', 'age']:
            if k not in json_.keys():
                raise Exception('Parameter '+k+' not specified.')
        if not create_party(**json_):
            raise Exception('Failed to create party. Try again later.')
        resp['data']['id'] = get_last_id()
    except Exception as e:
        resp['success'] = False
        resp['msg'] = e.args[0]

    return jsonify(resp)


@blueprint.route('/party/delete_party', methods=['DELETE'])
def delete_party_route():
    json_ = request.get_json(force=True)
    resp = {
        'success': True,
        'msg': 'Successfully deleted party.'
    }
    try:
        for k in ['id']:
            if k not in json_.keys():
                raise Exception('Parameter ' + k + ' not specified.')
        if not delete_party(id_=json_['id']):
            raise Exception('Failed to delete party. Try again later.')
    except Exception as e:
        resp['success'] = False
        resp['msg'] = e.args[0]

    return jsonify(resp)


@blueprint.route('/party/get_party_data/<int:id_>', methods=['GET', 'PATCH'])
def get_party_data_route(id_):
    resp = {
        "success": True,
        "msg": "Successfully retrieved party data.",
        "data": {}
    }
    try:
        if not id_:
            raise Exception('Party ID not specified')
        party_data = get_party_by_id(id_)
        if not party_data:
            raise Exception('Failed to get party data')
        resp['data'] = party_data
    except Exception as e:
        resp['success'] = False
        resp['msg'] = e.args[0]

    return jsonify(resp)


@blueprint.route('/party/get_all_parties', methods=['GET', 'PATCH'])
def get_all_parties_route():
    resp = {
        "success": True,
        "msg": "Successfully retrieved parties.",
        "data": []
    }
    try:
        party_data = get_all_parties()
        if not party_data:
            raise Exception('Failed to get parties')
        resp['data'] = party_data
    except Exception as e:
        resp['success'] = False
        resp['msg'] = e.args[0]

    return jsonify(resp)
