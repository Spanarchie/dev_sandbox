# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template, flash, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

# @app.route('/brief')
# def hello_world():
#     jsonList = getdata()
#     return render_template('brief.html')

# @app.route('/job')
# def hello_world():
#     jsonList = getdata()
#     return render_template('brief.html')

# @app.route('/task')
# def hello_world():
#     jsonList = getdata()
#     return render_template('brief.html')

# @app.route('/reportDash')
# def hello_world():
#     jsonList = getdata()
#     return render_template('brief.html')



app.run(debug=True)
