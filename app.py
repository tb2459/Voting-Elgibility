# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import vote_elegibility_determiner

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')
@app.route('/results', methods=["GET","POST"])
def results():
    age = int(request.form['age'])
    eligible = vote_elegibility_determiner(age)
    if(eligible):
        msg = "You are eligible to vote! Register now!"
    else:
        msg = "Sorry, not eligible. You will need to wait"+" "+str((18-age))+" "+"more years till you can vote."
    return render_template('results.html', message = msg)
