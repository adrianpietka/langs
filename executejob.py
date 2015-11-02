import sys
import argparse
import pymysql.cursors
from source.github import GitHub
from os import environ

if not __name__ == '__main__':
    print('Unsupported execution type.')
    sys.exit(0)

db_host = environ.get('DB_HOST', 'localhost')
db_user = environ.get('DB_USER', 'root')
db_password = environ.get('DB_PASSWORD', '')
db_database = environ.get('DB_DATABASE', 'fod')
db_charset = environ.get('DB_CHARSET', 'utf8mb4')

github_username = environ.get('GITHUB_USERNAME', '')
github_password = environ.get('GITHUB_PASSWORD', '')

parser = argparse.ArgumentParser(description="Future of development - Execute Job.")
parser.add_argument('job', help="job name to execute (available jobs: github-index, github-metadata)")
args = parser.parse_args()

try:
    connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_database, charset=db_charset, cursorclass=pymysql.cursors.DictCursor)

    if args.job == 'github-index':
        GitHub(connection, github_username, github_password).sync_index()
    elif args.job == 'github-metadata':
        GitHub(connection, github_username, github_password).sync_metadata(5000)
    else:
        print('Unsupported job name: {}'.format(args.job))
finally:
    connection.close()