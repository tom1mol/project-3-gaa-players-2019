import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route('/')
def hello():
    return 'fuck off'

if __name__ == "__main__":          
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 8080)), 
            debug=True)