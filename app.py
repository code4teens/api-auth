from flask import Flask

from api_auth import api_auth
from database import db_session

app = Flask(__name__)
app.register_blueprint(api_auth)


@app.teardown_appcontext
def close_session(exception=None):
    db_session.remove()
