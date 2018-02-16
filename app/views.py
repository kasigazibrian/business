
from flask import render_template, url_for, redirect, request, session, redirect, flash

from app import *

from app.forms import signupform, Loginform , BusinessRegistrationForm
from app.models import db, Signup, Login , BusinessRegistration
db.create_all()
@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    if request.method=='GET':

        return render_template("index.html", title='We Care!', button='Login')
    elif request.method=='POST':
        return redirect(url_for('registeredbusinesses'))
    else:
        return 'WRONG REQUEST'
@app.route('/login',methods=['GET','POST'])
def login():
    log = Loginform()

    if request.method=='GET':
        return render_template('login.html', form=log, title='Login!')
    elif request.method=='POST':
        Username = log.Username.data
        password = log.Password.data
        user = Login.query.filter_by(username=Username).first()
        if user:
            if(user.password == password):
                flash('You have successfully logged in!')
                session['user'] = user.id
                return redirect(url_for('registeredbusinesses'))

            else:
                flash('INVALID USERNAME OR PASSWORD')
                return render_template('login.html',form=log)
        else:
            flash('INVALID USERNAME OR PASSWORD')
            return render_template('login.html',form =log)
    else:
        return  'WRONG REQUEST'
@app.route('/logout', methods=['GET','POST'])
def logout():
    if request.method=='GET':
        flash('You have successfully logged out')
        return redirect(url_for('home'))

@app.route('/signup',methods=['GET','POST'])
def signup():
    sign = signupform()
    if request.method=='GET':
        return render_template('signup.html',form=sign, title='SignUp')
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
        return render_template('signup.html',form=sign, button='Login');

@app.route('/delete/<record_id>', methods=['GET','POST'])
def delete(record_id):
    if request.method=='GET':
        business_id = record_id
        user = BusinessRegistration.query.filter_by(business_id=business_id).first()
        ownerid = user.business_owner_id
        if session['user']!=None:
            if ownerid==session['user']:
            # delete_this = BusinessRegistration.query.filter_by(business_id=business_id).first()

                if user:
                    db.session.delete(user)
                    db.session.commit()
                    return redirect(url_for('registeredbusinesses'))
                else:
                    return 'Record doesnt exist'
            else:
                flash('You do not have enough privileges to delete this record')
                return redirect(url_for('registeredbusinesses'))
        else:
            flash('You need to login to delete!')
            return redirect(url_for('registeredbusinesses'))
    else:
        return 'Failed to delete record'
@app.route('/edit/<record_id>', methods=['GET','POST'])
def edit(record_id):
    business_registration_form = BusinessRegistrationForm()
    if request.method=='GET':
        business_id = record_id

        user = BusinessRegistration.query.filter_by(business_id=business_id).first()
        ownerid = user.business_owner_id
        if session['user']!=None:
            if ownerid==session['user']:
                if user:
                    business_registration_form.business_name.data= user.businessname
                    business_registration_form.business_street_address.data = user.business_street_address
                    business_registration_form.business_country.data = user.business_country
                    business_registration_form.business_city.data = user.business_city
                    business_registration_form.contact_number.data = user.contact_number
                    business_registration_form.email.data = user.email
                    business_registration_form.firstname.data = user.firstname
                    business_registration_form.lastname.data = user.lastname
                    business_registration_form.nominalcapital.data = user.nominalcapital
                    business_registration_form.business_category.data = user.business_cateogory

                    return render_template('edit.html', business_registration_form=business_registration_form, user=user,button='Logout')
                else:
                    return 'Record doesnt exist'
            else:
                flash('You do not have enough privileges to edit this record')
                return redirect(url_for('registeredbusinesses'))
        else:
            flash('You need to login to edit!')
            return redirect(url_for('registeredbusinesses'))
    elif request.method=='POST':
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
        business_id = record_id
        update_this = BusinessRegistration.query.filter_by(business_id=business_id).first()
        if update_this:
            update_this.businessname =business_name
            update_this.business_street_address = business_street_address
            update_this.business_country = business_country
            update_this.business_city = business_city
            update_this.contact_number = contact_number
            update_this.email = email
            update_this.firstname = firstname
            update_this.lastname = lastname
            update_this.nominal_capital = nominal_capital
            update_this.business_category = business_category
            db.session.commit()
            flash('Record updated successfully')
            return redirect(url_for('registeredbusinesses'))
        else:
            flash('Record doesnt exist')
            return redirect(url_for('registeredbusinesses'))

@app.route('/addbusiness', methods=['GET','POST'])
def addbusiness():
    business_registration_form = BusinessRegistrationForm()
    if request.method=='GET':
        return render_template('addbusiness.html', business_registration_form=business_registration_form, button='Logout')
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
        return render_template('registeredbusinesses.html',businesses=businesses, button='Logout')
@app.route('/testing', methods=['POST','GET'])
def testing():
    if request.method=='GET':
        return render_template('testing.html')