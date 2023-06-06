import json
from chatbot import *
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app,resources={r"/message/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/message/<string:message>')
def printm(message):
 return printmes(message)

app.run()