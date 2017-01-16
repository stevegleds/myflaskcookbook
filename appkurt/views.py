from flask import render_template
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
    return render_template('index.html', title='Home', user=user, posts=posts)
