from flask import Flask
from os import system

from modules.auth import blueprint as auth_blueprint
from modules.users import blueprint as users_blueprint


app = Flask(__name__)

app.register_blueprint(auth_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    system('@cls')
    app.run(port='8000')
