from flask import render_template
from . import main
from ..import db
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


