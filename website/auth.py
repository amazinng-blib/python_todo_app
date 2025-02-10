from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return "<p> Login</p>"

@auth.route("/logout", methods=["POST"])
def logout():
    return "<p> Logout</p>"

@auth.route("/register", methods=['GET', 'POST'])
def register():
    return "<p> Register</p>"