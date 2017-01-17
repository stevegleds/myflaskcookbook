from flask import render_template
from forms import LoginForm
from appkurt import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'TheKurtPrice'}
    # add fake database
    posts = [
        {'author': {'name': 'John Green'},
         'body': 'Papertowns is amazing'
         },
        {'author': {'name': 'Hang Green'},
         'body': 'Check out scishow'
         }
    ]
    return render_template("index.html",
                           title="Home",
                           posts=posts,
                           user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html",
                           title="Sign In",
                           form=form)
