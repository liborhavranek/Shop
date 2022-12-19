from flask import Blueprint,render_template, redirect, url_for, request, flash

views = Blueprint('views', __name__)




@views.route('/')
@views.route('/home')
def home():
    return render_template('index.html')