## main app

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


# test work will be removed
DISASTERS = [
    {
        'date': '1983.07.09 19:30',
        'type': 'earthquake',
        'location': 'Warsaw',
        'additional_info': 'nothing was the same ever since'
    },
    {
        'date': '2000.01.01 00:00',
        'type': 'earthquake',
        'location': 'World',
        'additional_info': 'Millenium bug'
    },   
    {
        'date': '2010.10.10 15:30',
        'type': 'earthquake',
        'location': 'Berlin',
        'additional_info': 'test data'
    },
]


# routing
@app.route('/test')
def test():
    return '<h1>Flask server is working<h1>'

@app.route('/ping', methods=['GET'])
def json_ping():
    return jsonify('pong')

@app.route('/disasters', methods=['GET'])
def all_disasters():
    return jsonify({
        'status': 'success',
        'disasters': DISASTERS
    })

# debug
if __name__=='__main__':
    app.run(debug=True)
