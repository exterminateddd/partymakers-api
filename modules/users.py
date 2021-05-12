from flask import Blueprint, request, session, jsonify

from user_control import *


blueprint = Blueprint("users", __name__)


@blueprint.route('/user/get_user_data/<string:username>', methods=['GET'])
def get_user_data_route(username: str):
    resp = {
        'success': True,
        'msg': 'Successfully retrieved user data.',
        'data': {}
    }
    try:
        if not username_taken(username):
            raise Exception('No account with provided username exists.')
        data = get_user_data(username)
        if not data:
            raise Exception('Failed to get data. Try again.')
        resp['data'] = {k: v for k, v in data.items() if k != '_id'}
    except Exception as e:
        resp['msg'] = e.args[0]
        resp['success'] = True
    return jsonify(resp)


@blueprint.route('/user/get_all_users', methods=['GET'])
def get_all_users_route():
    resp = {
        'success': True,
        'msg': '',
        'data': []
    }
    try:
        data = get_all_users()
        if not data:
            raise Exception('Failed to get all users. Try again.')
        resp['data'] = [{k: v for k, v in dict_.items() if k != '_id'} for dict_ in data]
    except Exception as e:
        resp['success'] = False
        resp['msg'] = e.args[0]
    return resp


@blueprint.route('/user/get_user_bookmarked_parties/<string:username>')
def get_user_bookmarked_parties_route(username):
    resp = {
        'success': True,
        'msg': 'Successfully retrieved parties.',
        'data': []
    }
    try:
        data = get_user_bookmarked_parties(username)
        if not data:
            raise Exception('Failed to get parties list. Try again.')
        resp['data'] = [{k: v for k, v in dict_.items() if k != '_id'} for dict_ in data]
    except Exception as e:
        resp['success'] = False
        resp['msg'] = e.args[0]
    return resp
