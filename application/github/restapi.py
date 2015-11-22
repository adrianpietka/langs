import requests

class GitHubRepositoryBlocked(Exception):
    pass

class GitHubInvalidResponse(Exception):
    pass

class GitHubRepositoryNotFound(Exception):
    pass

class GitHubRestApi:
    API_URL_REPOSITORIES = 'https://api.github.com/repositories?since={}'
    API_URL_REPOSITORY_METADATA = 'https://api.github.com/repos/{}'

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def _request_get(self, url):
        headers = {'User-Agent': 'Future of Development'}
        response = requests.get(url, headers=headers, 
            auth=(self.username, self.password)) if self.username != '' else  requests.get(url)
        if response.status_code == 403 and 'block' in response.json():
            raise GitHubRepositoryBlocked(url)
        if response.status_code == 404:
            raise GitHubRepositoryNotFound(url)
        if (response.status_code != 200):
            raise GitHubInvalidResponse('Invalid response for: {}. Status code: {}'.format(url, response.status_code))
        return response.json()

    def get_repositories(self, last_repository_id):
        return self._request_get(self.API_URL_REPOSITORIES.format(last_repository_id))

    def get_repository_metadata(self, full_name):
        return self._request_get(self.API_URL_REPOSITORY_METADATA.format(full_name))