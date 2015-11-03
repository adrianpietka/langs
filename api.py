import pymysql
import pprint
from flask import Flask, jsonify, g, render_template
from config import config

app = Flask(__name__)

def get_processed_repositories_number():
    with g.db.cursor() as cursor:
        sql = ('SELECT COUNT(*) AS total '
            'FROM github_index '
            'WHERE metadata_updated_at IS NOT NULL')
        cursor.execute(sql)
        result = cursor.fetchone()
        return result['total']

def get_repositories_number():
    with g.db.cursor() as cursor:
        sql = ('SELECT COUNT(*) AS total '
            'FROM github_index')
        cursor.execute(sql)
        result = cursor.fetchone()
        return result['total']

def get_oldest_repository():
    with g.db.cursor() as cursor:
        sql = ('SELECT full_name, created_at '
            'FROM github_index '
            'WHERE created_at IS NOT NULL '
            'ORDER BY created_at ASC')
        cursor.execute(sql)
        result = cursor.fetchone()
        return dict(name=result['full_name'], created=result['created_at'].isoformat())

def get_latest_repository():
    with g.db.cursor() as cursor:
        sql = ('SELECT full_name, created_at '
            'FROM github_index '
            'WHERE created_at IS NOT NULL '
            'ORDER BY created_at DESC')
        cursor.execute(sql)
        result = cursor.fetchone()
        return dict(name=result['full_name'], created=result['created_at'].isoformat())

@app.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/github/stats')
def github_stats():
    stats = dict(oldest=get_oldest_repository(), latest=get_latest_repository(),
        total=get_repositories_number(), processed=get_processed_repositories_number())
    return jsonify(data=stats)

@app.route('/github/languages')
def github_top_languages():
    sql = ('SELECT language, COUNT(*) AS `repositories`'
        'FROM github_index '
        'WHERE language IS NOT NULL '
        'GROUP BY language '
        'ORDER BY COUNT(*) DESC')
    with g.db.cursor() as cursor:
        cursor.execute(sql)
        return jsonify(data=cursor.fetchall())

@app.route('/github/new-repositories')
def github_new_repositories():
    sql = ('SELECT language, DATE(created_at) AS `created`, COUNT(*) AS `count` '
        'FROM github_index '
        'WHERE language IS NOT NULL '
        'GROUP BY language, DATE(created_at) '
        'ORDER BY language ASC, DATE(created_at) DESC')
    with g.db.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()
        aggregated = {}
        for item in results:
            if not item['language'] in aggregated:
                aggregated[item['language']] = []
            aggregated[item['language']].append({
                'date' : item['created'].isoformat(),
                'count' : item['count']
            })
        return jsonify(data=aggregated)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error='This API endpoint does not exist'), 404

@app.before_request
def before_request():
    g.db = pymysql.connect(host=config['db_host'], user=config['db_user'], password=config['db_password'], 
        db=config['db_database'], charset=config['db_charset'], cursorclass=pymysql.cursors.DictCursor)

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()