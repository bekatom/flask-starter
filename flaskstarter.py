from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

db = MongoEngine(app)

from views import *


if __name__ == '__main__':
    app.run()
