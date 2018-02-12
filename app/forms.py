from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextField, PasswordField, SubmitField, RadioField, FloatField, SelectField
from wtforms.validators import  EqualTo, Email, Length,InputRequired

class signupform(FlaskForm):
    Firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    Username = StringField('Username',validators=[InputRequired()])
    Password = PasswordField('Password', validators=[InputRequired(),EqualTo('Confirmpassword', message='Passwords must match')])
    Confirmpassword = PasswordField('Confirm Password', validators=[InputRequired(),Length(min=6,max=16)])
    Email = StringField('Email', validators=[InputRequired(), Email('Invalid Email')])
    Gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    Phonenumber = StringField('Phone Number')
    submit = SubmitField('Signup')

class Loginform(FlaskForm):
    Username = StringField('Username:', validators=[InputRequired()])
    Password = PasswordField('Password:',validators=[InputRequired()])
    remember = RadioField('Rememberme', choices=[('remeber_me','Remember me')])
    submit = SubmitField('Login')
#class EditForm(FlaskForm):

class BusinessRegistrationForm(FlaskForm):
    business_name = StringField('Company Name', validators=[InputRequired()])
    business_street_address= StringField('Company Street Address', validators=[InputRequired()])
    business_city = StringField('City', validators=[InputRequired()])
    business_country = StringField('Country', validators=[InputRequired])
    contact_number = StringField('Contact Number', validators=[InputRequired()])
    email = StringField('Email contact', validators=[InputRequired()])
    firstname = StringField('First Name',validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    nominalcapital = FloatField('Nominal Capital(UGX)', validators=[InputRequired()])
    business_category = SelectField('Business Category', choices=[('computers_electronics','Computers & Electronics'),('construction_contractors','Construction & Contractors'),('entertainment','Entertainment'),('food_dining','Food & Dining'),('health_medicine','Health & Medicine'),('real_estate','Real Estate')])
    submit = SubmitField('Register Business')

