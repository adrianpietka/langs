from api import app
from flask import jsonify

@app.route('/', methods=['GET'])
def hello():
    return jsonify(data='Hello World!')

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error='This API endpoint does not exist'), 404
