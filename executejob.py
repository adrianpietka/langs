import sys
import argparse
import pymysql.cursors
from os import environ

if not __name__ == '__main__':
    print('Unsupported execution type.')
    sys.exit(0)

db_host = environ.get('DB_HOST', 'localhost')
db_user = environ.get('DB_USER', 'root')
db_password = environ.get('DB_PASSWORD', '')
db_database = environ.get('DB_DATABASE', 'fod')
db_charset = environ.get('DB_CHARSET', 'utf8mb4')

parser = argparse.ArgumentParser(description="Future of development - Execute Job.")
parser.add_argument('job', help="job name to execute (available jobs: github)")
args = parser.parse_args()

#connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_database, charset=db_charset, cursorclass=pymysql.cursors.DictCursor)

if args.job == 'github':
    import jobs.github_trends
else:
    print('Unsupported job name: {}'.format(args.job))

#connection.close()