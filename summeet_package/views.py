import os
from flask import Blueprint, Response, Flask, session
from flask import request, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, request
from summeet_package.models import users
from werkzeug.security import generate_password_hash, check_password_hash
from summeet_package import db, create_app, app
from werkzeug.utils import secure_filename
from summeet_package.models import uploaded_files
from summeet_package.models import summarised_text
import text_sum as model_text_sum
import openai_whisper as model_text_transcript


app = Flask(__name__)
UPLOAD_FOLDER = 'audio_files_uploaded'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'mp4'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        user_email = request.form.get("user_email")
        age = request.form.get("age")
        pswd1 = request.form.get("pswd1")
        gender = request.form["gender"]
        # max_id = db.session.query(users).order_by(users.id.desc()).first()

        user = users.query.filter_by(user_email=user_email).first()
        if user:
            flash('Email already exists.', category='error')
            return render_template('user_registration.html')
        else:
            hashed_password = generate_password_hash(
                pswd1, method='sha256')
            user_regis = users(fname=fname, lname=lname, 
            user_email=user_email, password=hashed_password, 
            age=age, gender=gender)
            db.session.add(user_regis)
            db.session.commit()
            flash('Account created! Please login', category='success')
            return redirect(url_for('views.login'))
    return render_template('user_registration.html')

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pswd')
        user = users.query.filter_by(user_email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect('/user/dashboard')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template('login.html')


@views.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logged out successfully!", category='success')
    return redirect(url_for('views.home'))


@views.route('/user/dashboard', methods = ['GET', 'POST'])
@login_required
def user_dashboard():
    if current_user.fname == None:
        flash('Please login')
        return redirect(url_for('views.login'))
    else:
        name = current_user.fname
        # recmd_infl = model.recm_sys(name)
        # owner_id = current_user.id
        # advts_owner= uploaded_files.query.all()
        # advts = uploaded_files.query.filter_by(owner_id=owner_id)
        # advts_oid = uploaded_files.query.filter_by(owner_id=owner_id).first()
        # recmd_infl.remove(owner_id)
        # main=[]
        # for inf_id in recmd_infl:
        #     inf = users.query.filter_by(id=inf_id)
        #     for infl in inf:
        #         f = infl.fname
        #         l = infl.lname
        #         c = infl.categories
        #         s = infl.smh
        #         n = infl.infl_pic
        #         abc=[]
        #         abc.append(f)
        #         abc.append(l)
        #         abc.append(c)
        #         abc.append(s)
        #         abc.append(n)
        #         main.append(abc)
        # print(main)
        # try:
        #     # adv_oid = advts_oid.owner_id
        #     if adv_oid:
        #         return render_template('user_dashboard.html', name=name, advts_owner=advts_owner, adv_oid=adv_oid, owner_id=owner_id,main = main)
        #     else:
        #         return render_template('user_dashboard.html',advts=advts, name=name, advts_owner=advts_owner, owner_id=owner_id, main = main)
        # except:
        return render_template('user_dashboard.html', name=name)


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/user/upload', methods = ['GET', 'POST'])
@login_required
def user_upload():
    if current_user.fname == None:
        flash('Please login')
        return redirect(url_for('views.login'))
    else:
        if request.method == 'POST':
            files = request.files.getlist('mtng_file')
            for file in files:
                if file and allowed_file(file.filename):
                    user_fname = current_user.fname
                    email = current_user.user_email
                    meeting_name = request.form.get('meeting_name')
                    meeting_date = request.form.get('meeting_date')
                    email_list = request.form.get('mailing_list')
                    mailing_list = email_list.split(',')
                    meeting_agenda = request.form.get('meeting_agenda')
                    mtng_file = request.files['mtng_file']
                    owner_id = current_user.id
                    
                    filename = secure_filename(mtng_file.filename)
                    print(filename+' upload')
                    mimetype = mtng_file.mimetype
                    
                    file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
                    advt = uploaded_files(owner_id=owner_id, user_fname=user_fname, meeting_name=meeting_name, mailing_list=mailing_list, meeting_agenda=meeting_agenda, meeting_date=meeting_date, file_name = filename, mimetype=mimetype)
                    db.session.add(advt)
                    db.session.commit()
                    flash('Summarized successfully!', category='success')
                    return redirect(url_for('views.user_processing_summary'))
                else:
                    flash('Please enter all the details.')
                    user_email=current_user.user_email
                    user_fname = current_user.fname
                    return render_template('user_upload.html',user_email=user_email, user_name=user_fname)
        
        user_email=current_user.user_email
        user_name = current_user.fname
        return render_template('user_upload.html', user_email=user_email, user_name=user_name)

@views.route('/user/upload/processing_summary', methods = ['GET', 'POST'])
@login_required
def user_processing_summary():
    if current_user.fname == None:
        flash('Please login')
        return redirect(url_for('views.login'))
    else:
        owner_id = current_user.id
        up_file = uploaded_files.query.order_by(uploaded_files.id.desc()).first()
        file_name = up_file.file_name
        f_name = file_name[:-4]
        model_text_transcript.text_transcript(f_name)
        sum_text = model_text_sum.text_summ(f_name)
        summ_file = summarised_text(sum_text=sum_text, owner_id = owner_id)
        db.session.add(summ_file)
        db.session.commit()
        return redirect(url_for('views.user_summary'))

@views.route('/user/upload/summary', methods = ['GET', 'POST'])
@login_required
def user_summary():
    if current_user.fname == None:
        flash('Please login')
        return redirect(url_for('views.login'))
    else:
        user_fname = current_user.fname
        user_email=current_user.user_email
        up_file = uploaded_files.query.order_by(uploaded_files.id.desc()).first()
        file_name = up_file.meeting_name
        print(file_name)
        summ_text_tuple = summarised_text.query.order_by(summarised_text.id.desc()).first()
        summ_text = summ_text_tuple.sum_text
        
        return render_template('user_summary.html', user_email=user_email, up_file=up_file, user_name=user_fname, summ_text=summ_text)