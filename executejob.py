import sys
import argparse
import pymysql.cursors
from config import config
from source.github import GitHub

if not __name__ == '__main__':
    print('Unsupported execution type.')
    sys.exit(0)

parser = argparse.ArgumentParser(description="Future of development - Execute Job.")
parser.add_argument('job', help="job name to execute (available jobs: github-index, github-metadata)")
args = parser.parse_args()

try:
    connection = pymysql.connect(host=config['db_host'], user=config['db_user'], password=config['db_password'], 
        db=config['db_database'], charset=config['db_charset'], cursorclass=pymysql.cursors.DictCursor)

    if args.job == 'github-index':
        GitHub(connection, config['github_username'], config['github_password']).sync_index()
    elif args.job == 'github-metadata':
        GitHub(connection, config['github_username'], config['github_password']).sync_metadata(1000)
    else:
        print('Unsupported job name: {}'.format(args.job))
finally:
    connection.close()