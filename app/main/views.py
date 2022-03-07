from flask import render_template,request,redirect,url_for,abort
from . import mainBlueprint
from ..import db


#views
@mainBlueprint.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title ='Pitches'
    return render_template('index.html', title=title)


# @mainBlueprint.route('/pitch')
# def pithes():

#     return render_template('pitches.html')