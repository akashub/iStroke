from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getprediction', methods=['GET'])
def get_prediction():
    testjson = {'prediction': 0.5}
    return jsonify(testjson)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)