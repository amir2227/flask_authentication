from flask import Blueprint, render_template, redirect, url_for
from flask.globals import request

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


#@auth.route('/login', methods=['POST'])
#def login_post():

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup' , methods=['POST'])
def signup_post():
    user_name = request.form.get('user_name')
    full_name = request.form.get('full_name')
    password = request.form.get('password')

    

@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))
