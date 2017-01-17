from flask import Flask
import wtforms
app = Flask(__name__)
app.config.from_object('config') #  Loads settings in config.py file
from appkurt import views
