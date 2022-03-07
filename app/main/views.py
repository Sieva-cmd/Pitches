from flask import render_template,request,redirect,url_for,abort
from . import main
from ..import db, photos
from ..models import User,Pitch
from flask_login import login_required,current_user
from .forms import UpdateProfile,PitchForm
import datetime


#views
@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''

    pitches = Pitch.query.all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    interview = Pitch.query.filter_by(category = 'Interview').all() 
    sports = Pitch.query.filter_by(category = 'Sports').all()
    technology = Pitch.query.filter_by(category = 'Technology').all() 
    title ='Pitches'
    return render_template('index.html', title=title,interview = interview,sports = sports, pitches = pitches,promotion= promotion,technology=technology)


@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        
        new_pitch = Pitch(title = title,post=post,category=category,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
        
    return render_template('new_pitch.html', form = form)    


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    posts = Pitch.query.filter_by(user = current_user).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)    


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
