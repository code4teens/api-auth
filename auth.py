import bcrypt
from flask import Blueprint, request

from models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    id = request.json.get('id')
    user = User.query.filter_by(id=id).one_or_none()

    if user is not None:
        password = request.json.get('password')

        if password is not None:
            if bcrypt.checkpw(
                password.encode('utf-8'),
                user.password.encode('utf-8')
            ):
                data = {
                    'title': 'OK',
                    'status': 200,
                    'detail': f'User {id} logged in'
                }

                return data, 200
            else:
                data = {
                    'title': 'Unauthorised',
                    'status': 401,
                    'detail': f'Wrong password for user {id}'
                }

                return data, 401
        else:
            data = {
                'title': 'Bad Request',
                'status': 400,
                'detail': 'Password missing'
            }

            return data, 400

    else:
        data = {
            'title': 'Not Found',
            'status': 404,
            'detail': f'User {id} not found'
        }

        return data, 404
