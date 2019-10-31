## main app

from flask import Flask

app = Flask(__name__)

# routing
@app.route('/test')
def test():
    return '<h1>Flask server is working<h1>'

# debug
if __name__=='__main__':
    app.run(debug=True)
