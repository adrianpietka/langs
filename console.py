import sys
import argparse
import pymysql.cursors
from config import config
from application.source.github import GitHub
from application.commands.prepare_database_sharding import PrepareDatabaseSharding

if not __name__ == '__main__':
    print('Unsupported execution type.')
    sys.exit(0)

parser = argparse.ArgumentParser(description="Future Of Development - Execute Command.")
parser.add_argument('command', help="command to execute (available: github-index, github-metadata, prepare-database-sharding)")
args = parser.parse_args()

try:
    connection = pymysql.connect(host=config['db_host'], user=config['db_user'], password=config['db_password'], 
        db=config['db_database'], charset=config['db_charset'], cursorclass=pymysql.cursors.DictCursor)

    if args.command == 'prepare-database-sharding':
        PrepareDatabaseSharding(connection).execute()
    elif args.command == 'github-index':
        GitHub(connection, config['github_username'], config['github_password']).sync_index()
    elif args.command == 'github-metadata':
        GitHub(connection, config['github_username'], config['github_password']).sync_metadata(1000)
    else:
        print('Unsupported command: {}'.format(args.command))
finally:
    connection.close()