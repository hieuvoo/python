from flask import Flask, render_template, redirect, request, session, flash
import re, bcrypt
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'tamales'
mysql = MySQLConnector(app,'walldb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    print dir(bcrypt)
    return render_template('index.html')

@app.route('/register', methods=['Post'])
def register():
    flag = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email')
        flag = False
    if len(request.form['first_name']) < 2:
        flash('First name must be at least 2 characters long')
        flag = False
    if len(request.form['last_name']) < 2:
        flash('Last name must be at least 2 characters long')
        flag = False
    if not request.form['first_name'].isalpha():
        flash('First name must be a-z')
        flag = False
    if not request.form['last_name'].isalpha():
        flash('Last name must be a-z')
        flag = False
    if request.form['password'] != request.form['c_password']:
        flash('Password and Confirm password do not match')
        flag = False
    if len(request.form['password']) < 8:
        flash('Password must be at least 9 characters')
        flag = False
    #if email is unique
    query = "SELECT * FROM users where email = :email"
    data = {'email': request.form['email']}
    if mysql.query_db(query,data):
        flash('Email already in use')
        flag = False
    
    if flag:
        #save to database
        print "Info was valid"
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(),NOW())"

        hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : hashed   
        }
        session['user_id'] = mysql.query_db(query, data)

        return redirect('/wall')
    else:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    flag = True

    if len(request.form['email']) < 1:
        flag = False
        flash('You must put a email')
    if len(request.form['password']) < 1:
        flag = False
        flash('You must put a password')
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email')
        flag = False
    
    if flag:
        query = 'SELECT * FROM users where email = :email'
        data = {'email': request.form['email']}
        user = mysql.query_db(query,data)
        if user:
            #validate password
            if bcrypt.checkpw(request.form['password'].encode('utf-8'), user[0]['password'].encode('utf-8')):
                session['user_id'] = user[0]['id']
                return redirect('/wall')
            else:
                flash('Invalid password')
                return redirect('/')
        else:
            flash('User not found')
            return redirect('/')            
    else:
        return redirect('/')

@app.route('/wall')
def the_wall():
    if 'user_id' in session:
        query = 'SELECT * FROM users where id = :id'
        data = {'id': session['user_id']}
        l_user = mysql.query_db(query,data)

        query2 = 'SELECT users.id AS user_id, messages.id AS m_id, messages.message, users.first_name, users.last_name, messages.created_at from messages JOIN users ON messages.user_id = user_id'
        messages = mysql.query_db(query2)

        query3 = "SELECT users.id AS user_id, comments.id AS c_id, comments.comment, comments.message_id, users.first_name, users.last_name, comments.created_at from comments JOIN users ON comments.user_id = users.id"
        comments = mysql.query_db(query3)

        return render_template('wall.html', l_user=l_user[0], messages=messages, comments=comments)
    else:
        print "Go back to where you came from"
        return redirect('/')

@app.route('/create_message', methods=['Post'])
def save_message(): 
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {'user_id': session['user_id'],
            'message': request.form['message'],
    }
    mysql.query_db(query,data)
    return redirect('/wall')

@app.route('/create_comments', methods=['POST'])
def save_comment():
    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    data = {'user_id': session['user_id'],
            'message_id': request.form['message_id'],
            'comment': request.form['comment']
    }
    mysql.query_db(query,data)
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)