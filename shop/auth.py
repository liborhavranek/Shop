from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def log_in():
    return 'login'

@auth.route('/register')
def register():
    return 'register'

@auth.route('/logout')
def log_out():
    return 'login'

@auth.route('/delete_user')
def delete_user():
    return 'delete_user'