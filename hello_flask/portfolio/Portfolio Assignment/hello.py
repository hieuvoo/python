from flask import Flask, render_template   # render_template to allow us to render index.html.
app = Flask(__name__)    
                        
@app.route('/')                            # Global variable __name__ tells Flask whether or not we
                                           # are running the file directly or importing it as a module.         
      
def hello_world():
  return render_template('index.html')

# @app.route('/success')
# def success():
#   return render_template('success.html')   

app.run(debug=True)      