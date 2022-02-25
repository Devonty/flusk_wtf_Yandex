from flask import Flask, render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from LoginForm import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'что я тут напишу - это моё дело'

@app.route('/')
@app.route('/index')
def index(title='name'):
    return render_template('task_1.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('task_2.html',prof=prof, title='На марс')


@app.route('/list_prof/<param>')
def list_prof(param):
    list_ = [f'Профессия{i}' for i in range(16)]
    return render_template('task_3.html',param=param, title='На марс', list_=list_)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')