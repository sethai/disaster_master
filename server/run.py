## main app

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from models import *

# configuration
DEBUG = True

# app instance
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# routing
@app.route('/test')
def test():
    return '<h1>Flask server is working<h1>'

@app.route('/ping', methods=['GET'])
def json_ping():
    return jsonify('pong')

@app.route('/disasters', methods=['GET'])
def all_disasters():
    dis_type = []
    ## TODO return stuff dependant on the selected types
    param_list = request.args.get('type')
    print(param_list)
    dis_type = param_list.split(",")
    get_data(dis_type)
    with open('disasters.json', encoding="utf-8") as disasters_file:
        DISASTERS = json.load(disasters_file)
    return jsonify({
        'status': 'success',
        'disasters': DISASTERS
    })

# debug
if __name__=='__main__':
    app.run()
