from flask import render_template
from appkurt import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'TheKurtPrice'}
    return render_template('index.html', title='Home', user=user)
