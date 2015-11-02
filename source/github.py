import requests
from datetime import datetime

class GitHub:
    def __init__(self, db, github_username, github_password):
        self.db = db
        self.github_username = github_username
        self.github_password = github_password

    def convertDateTime(self, value):
        try:
            dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
            return dt.__format__('%Y-%m-%d %H:%M:%S')
        except:
            return value

    def get_repository_to_update_metadata(self, limit):
        with self.db.cursor() as cursor:
            cursor.execute('SELECT id, full_name FROM github_index ORDER BY metadata_updated_at ASC, id DESC LIMIT %s', (limit))
            return cursor.fetchall()

    def get_last_repository_id(self):
        with self.db.cursor() as cursor:
            cursor.execute('SELECT id FROM github_index ORDER BY id DESC LIMIT 1')
            result = cursor.fetchone()
            return result['id'] if result != None else 0

    def update_repository_metadata(self, id, metadata):
        with self.db.cursor() as cursor:
            sql = ('UPDATE github_index SET '
                'metadata_updated_at = NOW(), '
                'created_at = %s, '
                'pushed_at = %s, '
                'language = %s, '
                'stargazers_count = %s, '
                'watchers_count = %s, '
                'forks_count = %s, '
                'network_count = %s '
                'WHERE id = %s')
            values = (self.convertDateTime(metadata['created_at']), self.convertDateTime(metadata['pushed_at']),
                metadata['language'], metadata['stargazers_count'],
                metadata['watchers_count'], metadata['forks_count'],
                metadata['network_count'], id)
            cursor.execute(sql, values)
        self.db.commit();

    def add_repository(self, repository):
        with self.db.cursor() as cursor:
            sql = 'INSERT INTO github_index (id, full_name, owner_login, description) VALUES(%s, %s, %s, %s)'
            values = (int(repository['id']), repository['full_name'], repository['owner']['login'], repository['description'])
            cursor.execute(sql, values)
        self.db.commit()

    def request_get(self, url):
        response = requests.get(url, auth=(self.github_username, self.github_password)) if self.github_username != '' else  requests.get(url)
        if (response.status_code != 200):
            raise Exception('Invalid response. Status code: {}'.format(response.status_code))
        return response

    def get_repositories(self, last_repository_id):
        return self.request_get('https://api.github.com/repositories?since={}'.format(last_repository_id)).json()

    def get_repository_metadata(self, full_name):
        return self.request_get('https://api.github.com/repos/{}'.format(full_name)).json()
    
    def sync_index(self):
        print('GitHub - sync index of repositories')
        repositories = self.get_repositories(self.get_last_repository_id())
        for repository in repositories:
            print('Repository #{}: {}'.format(repository['id'], repository['full_name']))
            self.add_repository(repository)
        
    def sync_metadata(self, limit):
        print('GitHub - sync metadata of repositories')
        repositories = self.get_repository_to_update_metadata(limit)
        for repository in repositories:
            print('Repository #{}: {}'.format(repository['id'], repository['full_name']))
            metadata = self.get_repository_metadata(repository['full_name'])
            self.update_repository_metadata(repository['id'], metadata)