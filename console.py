import sys
import argparse
import pymysql.cursors
from application.github import *
from application.commands import *
from application.repositories import *
from application.config import config

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
        repository = IndexRepository(connection)
        api = GitHubRestApi(config['github_username'], config['github_password'])
        GitHubBuildIndex(repository, api).execute();
    elif args.command == 'github-metadata':
        repository = IndexRepository(connection)
        api = GitHubRestApi(config['github_username'], config['github_password'])
        GitHubUpdateMetadata(repository, api).execute();
    else:
        print('Unsupported command: {}'.format(args.command))
finally:
    connection.close()