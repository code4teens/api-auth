from flask import Flask

from auth import auth
from database import db_session

app = Flask(__name__)
app.register_blueprint(auth)


@app.teardown_appcontext
def close_session(exception=None):
    db_session.remove()
