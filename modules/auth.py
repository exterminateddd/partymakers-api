from flask import Blueprint, request, session, jsonify

from user_control import register_user, username_taken, check_login
from utils import valid_password


blueprint = Blueprint("auth", __name__)


def set_session_user(username: str) -> None:
    session.__setitem__('current_user', username)


def get_session_user() -> str or None:
    return session.__getattribute__('current_user')


@blueprint.route('/auth/register_user', methods=['POST'])
def register_user_route():
    resp = {
        'success': True,
        'msg': 'Registration Successful'
    }
    try:
        json_ = {k: v for k, v in request.get_json(force=True).items() if k and v}
        for k in ['username', 'password', 'firstName', 'lastName']:
            if k not in json_.keys():
                raise Exception("Missing parameter '"+k+"'")
            elif type(json_[k]) != str:
                raise Exception('Parameter '+k+' is of wrong type')
        if username_taken(json_['username']):
            raise Exception('Provided username is already taken. Please try another one.')
        valid = valid_password(json_['password'])
        if not valid['valid']:
            raise Exception(valid['reason'])
        register = register_user(**json_)
        if not register:
            raise Exception('Registration failed. Try again later.')
        set_session_user(json_['username'])
    except Exception as e:
        print(e)
        resp['success'] = False
        resp['msg'] = e.args[0]
    return jsonify(resp)


@blueprint.route('/auth/attempt_login', methods=['POST'])
def attempt_login_route():
    resp = {
        'success': True,
        'msg': 'Login Successful'
    }
    try:
        json_ = {k: v for k, v in request.get_json(force=True).items() if k and v}
        for k in ['username', 'password']:
            if k not in json_.keys():
                raise Exception("Missing parameter '" + k + "'")
            elif type(json_[k]) != str:
                raise Exception('Parameter ' + k + ' is of wrong type')
        if not username_taken(json_['username']):
            raise Exception('No account with provided username exists. Check it and try again.')
        login = check_login(**json_)
        if not login:
            raise Exception('Login failed. Your password may be wrong.')
        set_session_user(json_['username'])
    except Exception as e:
        resp['success'] = False
        resp['msg'] = e.args[0]
    return jsonify(resp)


@blueprint.route('/auth/get_current_user', methods=['GET'])
def get_current_user_route():
    resp = {
        "success": True,
        "data": ""
    }
    try:
        resp['data'] = get_session_user()
    except Exception as e:
        resp['success'] = False

    return jsonify(resp)
