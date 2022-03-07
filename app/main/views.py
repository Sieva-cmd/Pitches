from flask import render_template,request,redirect,url_for,abort
from . import main
from ..import db
from ..models import User
from flask_login import login_required


#views
@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title ='Pitches'
    return render_template('index.html', title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)    


