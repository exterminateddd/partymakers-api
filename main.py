from flask import Flask, session, Response, request, jsonify
from os import system

from modules.auth import blueprint as auth_blueprint
from modules.users import blueprint as users_blueprint


app = Flask(__name__)
app.secret_key = 'secret_key'

app.register_blueprint(auth_blueprint)
app.register_blueprint(users_blueprint)


@app.before_request
def before_req():
    if 'current_user' not in session:
        if 'auth' not in str(request.endpoint):
            return jsonify({
                "success": False,
                "msg": "Not Authorized"
            }), 403


@app.after_request
def after_req(resp):
    resp.headers.add("Access-Control-Allow-Origin", "*")

    return resp


if __name__ == '__main__':
    system('@cls')
    app.run(port='8000')
