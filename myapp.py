import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    jsonMessage = {}
    dataObject = {} 
    dataObject['height'] = 181
    dataObject['weight'] = 65
    dataObject['age'] = 22

    jsonMessage['message'] = 'Hello World'
    jsonMessage['data'] = dataObject
    return jsonify(jsonMessage)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)