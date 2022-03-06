from flask import render_template
from . import main
from  ..models import Pitch


#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title ='Pitches'
    return render_template('index.html', title=title)


@main.route('/pitch')
def pithes():

    return render_template('pitches.html')