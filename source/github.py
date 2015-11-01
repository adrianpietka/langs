import requests

class GitHub:
    def __init__(self, db):
        self.db = db

    def get_last_repository(self):
        return {'id' : 1, 'full_name' : 'adrianpietka/langs'}

    def add_repository(self, repository):
        print('Insert repository #{} to DB'.format(repository['id']))

    def request_get(self, url):
        response = requests.get(url)

        if (response.status_code != 200):
            raise Exception('Invalid response. Status code: {}'.format(response.status_code))

        return response

    def get_repositories(self, last_repository_id):
        return self.request_get('https://api.github.com/repositories?since={}'.format(last_repository_id)).json()

    def get_repository_metadata(self, full_name):
        return self.request_get('https://api.github.com/repos/{}'.format(full_name)).json()
    
    def sync_repositories(self):
        print('Sync new repositories from GitHub')
        last_repository = self.get_last_repository()
        repositories = self.get_repositories(last_repository['id'])
        for repository in repositories:
            print('Repo #{}: {}'.format(repository['id'], repository['full_name']))
            self.add_repository(repository)
        
    def sync_metadata(self):
        print('Sync metadata for new repositories of GitHub')
        repository = self.get_last_repository()
        metadata = self.get_repository_metadata(repository['full_name'])
        for key in metadata:
            print('{} : {}'.format(key, metadata[key]))

    def execute(self):
        self.sync_repositories()
        self.sync_metadata()