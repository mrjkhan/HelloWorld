from flask import Flask, render_template, request, jsonify, redirect
from flask import send_file

import pandas as pd
import json
import os.path
from os import path
import datetime


##additional imports

with open('./data/users.json') as json_data:
        users = json.load(json_data)

app = Flask(__name__)


####functions



##route decorator
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        status = ""
        return render_template("index.html", status=status)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users[username]==password:
            status = ""
            print(username)
            print(password)
            url = 'https://guarded-garden-81041.herokuapp.com'
            return redirect(url)
        else:
            status="That username and password combination is not correct"
            return render_template("index.html", status = status)



if __name__ == '__main__':
   app.run("0.0.0.0:5000", debug=True)
