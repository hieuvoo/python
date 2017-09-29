from flask import Flask, render_template, redirect, request, session
from mysqlconnection import MySQLConnector
import re
from datetime import datetime


app = Flask(__name__)
mysql = MySQLConnector(app,'users') # make a new db??
app.secret_key = 'key'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'valid' not in session:
        session['valid'] = True
    return render_template('index.html')

@app.route('/process' , methods=['POST'])
def process():
    if not re.match('[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})', request.form['email']):
        session['valid'] = False
        return redirect('/')
    else:
        query = "INSERT INTO emails(email,created_at,updated_at) VALUES (:email,NOW(),NOW())"
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query,data)
        session['valid'] = True
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails_db = mysql.query_db(query)
    return render_template('success.html', emails=emails_db)

app.run(debug=True)
