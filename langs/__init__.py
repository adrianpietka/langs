from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello():
    return jsonify(data='Hello World!')

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error='This API endpoint does not exist'), 404

if __name__ == '__main__':
    app.run()