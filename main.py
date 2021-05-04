from flask import Flask

from auth import blueprint as auth_blueprint


app = Flask(__name__)

app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(port='8000')
