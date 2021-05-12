from flask import Blueprint, request, session, jsonify

from party_control import *


blueprint = Blueprint("auth", __name__)


@blueprint.route('/create_party', methods=['POST'])
def create_party_route():
    json_ = request.get_json(force=True)
    resp = {
        'success': True,
        'msg': 'Successfully created party.'
    }
    try:
        for k in ['name', 'desc', 'date', 'coordinates', 'location_main', 'location_add', 'price', 'age']:
            if k not in json_.keys():
                raise Exception('Parameter '+k+' not specified.')
        if not create_party(**json_):
            raise Exception('Failed to create party. Try again later.')
    except Exception as e:
        resp['success'] = False
        resp['msg'] = e.args[0]

    return jsonify(resp)


@blueprint.route('/delete_party', methods=['DELETE'])
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
