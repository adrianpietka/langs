import pymysql
import pprint
from flask import Flask, jsonify, g
from config import config

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(data='Hello World!')

@app.route('/github/top-ten')
def github_top_languages():
    sql = ('SELECT language, COUNT(*) AS `score`'
        'FROM github_index '
        'WHERE language IS NOT NULL '
        'GROUP BY language '
        'ORDER BY COUNT(*) DESC '
        'LIMIT 10')
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