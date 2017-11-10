from flask import Flask, render_template

app = Flask(__name__)
app.debug = True #TODO remove this from live

# This route is to get form input from html page
@app.route('/', methods=['GET'])
def dropdown():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('test.html', colours=colours)

if __name__ == '__main__':
    app.run()
