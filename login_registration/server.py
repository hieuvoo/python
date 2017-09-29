from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a.zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secretkey
mysql = MySQLConnector(app,'login_reg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    print request.form
    errors = []
    
    if len(request.form['first_name']) < 1:
        errors.append('First name is required')
    elif not request.form['first_name'].isalpha():
        errors.append
    elif len(request.form['first_name']) < 2:
        errors.append('First name must be 2 characters or longer.')

    if len(request.form['last_name']) < 1:
        errors.append('last name is required')
    elif len(request.form['last_name']) < 2:
        errors.append('last name must be 2 characters or longer.')

    if len(request.form['email']) < 1:
        errors.append('Email is required')
    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append('invalid email')
    else:
        query = 'SELECT * FROM users WHERE email = :email'
        user = mysql.query_db(query, {'email': request.form['email'].lower()})
        if len(user) > 0:
            errors.append('email already in use.')
    
    if len(request.form['password']) < 1:
        errors.append('password required')
    elif len(request.form['password']) < 8:
        errors.append('password must be 8 characters or more')

    if len(request.form['confirm_password']) < 1:
        errors.append('confirm password required')
    elif len(request.form['confirm_password']) != request.form['password']
        errors.append('confirm password must match password')

    if len(errors) > 0:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
        data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'].lower(),
            'password': bcrypt.hashpw(request.form['password'],.encode(), bcrypt.gensalt())
        }
        user_id = mysql.query_db(query, data)
        user = mysql.query_db('SELECT * FROM users WHERE id = {}'.format(user_id))
        session['user'] = user_id, user['first_name']
        return redirect('/wall')

        # ______________________
@app.route('/login', methods=['POST'])
def login():
    errors = []
    
    if len(request.form['email']) < 1:
        errors.append('Email is required')
    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append('invalid email')
    else:
        query = 'SELECT * FROM users WHERE email = :email'
        user = mysql.query_db(query, {'email': request.form['email'].lower()})
        if len(user) > 0:
            errors.append('unknown email.')
    
    if len(request.form['password']) < 1:
        errors.append('password required')
    elif len(request.form['password']) < 8:
        errors.append('password must be 8 characters or more')

    if len(errors) > 0:
        for error in errors:
            flash(error)
        return redirect('wall.html')
    else:
        if bcrypt.checkpw(request.form['password'].encode(), user[0][password].encode()):
            flash('successfully logged in')
            
        else:
            flash('incorrect password')

    return redirect('/')

@app.route('/wall')
def wall():
    if 'user' not in session:
        flash('you must login or register first')
        return redirect('/') 
    return render_template('wall.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')

app.run(debug=True)