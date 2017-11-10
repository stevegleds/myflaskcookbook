from flask import Flask
#  This is just a placeholder. No links to other files in this project as at 17 January 2017
app = Flask(__name__)
app.debug = True #TODO remove this from live

@app.route('/')
def hello_world():
    return 'Hello World!!'

if __name__ == '__main__':
    app.run()
