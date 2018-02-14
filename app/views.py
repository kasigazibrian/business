
from flask import render_template, url_for, redirect, request, session, redirect

from app import *

from app.forms import signupform, Loginform , BusinessRegistrationForm
from app.models import db, Signup, Login , BusinessRegistration
db.create_all()
@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    if request.method=='GET':
        allusers = BusinessRegistration.query.all()
        return render_template("index.html", users=allusers)
@app.route('/login',methods=['GET','POST'])
def login():
    log = Loginform()

    if request.method=='GET':
        return render_template('login.html', form=log)
    elif request.method=='POST':
        Username = log.Username.data
        password = log.Password.data
        message = 'INVALID USERNAME OR PASSWORD'
        message1 ='You have successfully logged in!'
        user = Login.query.filter_by(username=Username).first()
        if user:
            if(user.password == password):
                session['user'] = user.id
                return redirect(url_for('addbusiness'))

            else:
                return render_template('login.html',form=log, message=message)
        else:
            return render_template('login.html',form =log, message=message)
    else:
        return  'WRONG REQUEST'
@app.route('/signup',methods=['GET','POST'])
def signup():
    sign = signupform()
    if request.method=='GET':
        return render_template('signup.html',form=sign)
    elif request.method=='POST':
        Firstname = sign.Firstname.data
        Lastname = sign.lastname.data
        Username = sign.Username.data
        Password = sign.Password.data
        Phonenumber = sign.Phonenumber.data
        Email = sign.Email.data
        Gender = sign.Gender.data
        data1 = Signup(firstname=Firstname,lastname=Lastname,username=Username,password=Password,phonenumber=Phonenumber,email=Email,gender=Gender)
        db.session.add(data1)
        data2 = Login(username=Username, password=Password)
        db.session.add(data2)
        db.session.commit()
        return 'Successfully signed up'
    else:
        return render_template('signup.html',form=sign);

@app.route('/delete/<record_id>', methods=['GET','POST'])
def delete(record_id):
    if request.method=='GET':
        Username = record_id
        delete_this = Signup.query.filter_by(username=Username).first()
        if delete_this:
            db.session.delete(delete_this)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return 'Record doesnt exist'
    else:
        return 'Failed to delete record'
@app.route('/details/<record_id>',methods=['GET','POST'])
def details(record_id):
    if request.method=='GET':
        details_for = Signup.query.filter_by(username=record_id).first()
        if details_for:
            return render_template('details.html',details_for =details_for)
        else:
            return 'The record doesnt exist'
    else:
        return 'Failed to view the details of the record'
@app.route('/edit/<record_id>', methods=['GET','POST'])
def edit(record_id):
    if request.method=='GET':
        details_for = Signup.query.filter_by(username=record_id)
        if details_for:
            return  render_template('details.html', details_for=details_for)
        else:
            return 'The record doesnt exist'
    if request.method=='POST':
        pass
@app.route('/addbusiness', methods=['GET','POST'])
def addbusiness():
    business_registration_form = BusinessRegistrationForm()
    if request.method=='GET':
        return render_template('addbusiness.html', business_registration_form=business_registration_form)
    elif request.method =='POST':
        business_name = business_registration_form.business_name.data
        business_street_address = business_registration_form.business_street_address.data
        business_country = business_registration_form.business_country.data
        business_city = business_registration_form.business_city.data
        contact_number = business_registration_form.contact_number.data
        email = business_registration_form.email.data
        firstname = business_registration_form.firstname.data
        lastname = business_registration_form.lastname.data
        nominal_capital = business_registration_form.nominalcapital.data
        business_category = business_registration_form.business_category.data
        user_id = session['user']
        business_info = BusinessRegistration(businessname=business_name,business_street_address=business_street_address,business_city=business_city,business_country=business_country,
                                             contact_number=contact_number,email=email,firstname=firstname,lastname=lastname,nominalcapital=nominal_capital,business_category=business_category, business_owner_id=user_id)
        db.session.add(business_info)
        db.session.commit()
        return 'successfullyadded'

    else:
        return 'WRONG REQUEST'
@app.route('/registeredbusinesses', methods=['POST','GET'])
def registeredbusinesses():
    businesses = BusinessRegistration.query.all()
    if request.method=='GET':
        return render_template('registeredbusinesses.html',businesses=businesses)
