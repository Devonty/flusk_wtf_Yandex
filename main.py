from flask import Flask, url_for, request, render_template
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from LoginForm import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'что я тут напишу - это моё дело'

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('task_1.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('task_2.html',prof=prof, title='На марс')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
