from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    try:
        session['count'] += 1
    except:
        session['count'] = 1 
    return render_template('index.html')

@app.route('/two', methods=['POST'])
def two():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0 
    return redirect('/')

app.run(debug=True)