from flask import Flask, request

app = Flask(__name__)


@app.route('/whatismyname', methods = ['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        return 1/0
    elif request.method == 'POST':
        return 'creating your name'
    elif request.method == 'DELETE':
        a = 1/0
        return a

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)