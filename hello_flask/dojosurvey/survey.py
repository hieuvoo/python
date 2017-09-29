from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def survey():
    if len(request.form['name']) < 1:
        flash('Please fill in your name.')
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash('Please enter a comment.')
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash('Comment cannot be more than 120 characters.')
        return redirect('/')
    else:
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        language = request.form['language']
        comment = request.form['comment']
        return render_template('result.html',name=name,location=location,language=language,comment=comment)

app.run(debug=True)                