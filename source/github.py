import requests

class GitHub:
    def __init__(self, db, github_username, github_password):
        self.db = db
        self.github_username = github_username
        self.github_password = github_password

    def get_repository_to_update_metadata(self, limit):
        with self.db.cursor() as cursor:
            cursor.execute('SELECT id, full_name FROM github_index ORDER BY metadata_updated_at ASC LIMIT %s', (limit))
            return cursor.fetchall()

    def get_last_repository_id(self):
        with self.db.cursor() as cursor:
            cursor.execute('SELECT id FROM github_index ORDER BY id DESC LIMIT 1')
            result = cursor.fetchone()
            return result['id'] if result != None else 0

    def update_repository_metadata(self, id, metadata):
        with self.db.cursor() as cursor:
            cursor.execute('UPDATE github_index SET metadata_updated_at = NOW() WHERE id = %s', (id))
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
        
    def sync_metadata(self):
        print('GitHub - sync metadata of repositories')
        repositories = get_repository_to_update_metadata()
        for key in repositories:       
            repository = repositories[key]
            metadata = self.get_repository_metadata(repository['full_name'])
            update_repository_metadata(repository['id'], metadata)