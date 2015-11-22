import pymysql
import pprint
from flask import Flask, jsonify, g, render_template
from application.config import config
from application.repositories import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/github/stats')
def github_stats():
    stats = dict(oldest=g.index_repository.get_oldest_repository(),
        latest=g.index_repository.get_latest_repository(),
        total=g.index_repository.get_repositories_number(),
        processed=g.index_repository.get_processed_repositories_number())
    return jsonify(data=stats)

@app.route('/github/languages')
def github_languages():
    return jsonify(data=g.index_repository.get_all_languages())

@app.route('/github/languages/stats')
def github_languages_stats():
    return jsonify(data=g.index_repository.get_languages_stats())

@app.route('/github/new-repositories/monthly')
def github_new_repositories_monthly():
    return jsonify(data=g.index_repository.new_repositories_monthly())

@app.route('/github/new-repositories/yearly')
def github_new_repositories_yearly():
    return jsonify(data=g.index_repository.new_repositories_yearly())

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error='This API endpoint does not exist'), 404

@app.before_request
def before_request():
    g.db = pymysql.connect(host=config['db_host'], user=config['db_user'], password=config['db_password'], 
        db=config['db_database'], charset=config['db_charset'], cursorclass=pymysql.cursors.DictCursor)
    g.index_repository = IndexRepository(g.db)

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()