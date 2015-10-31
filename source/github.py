import requests

# mock
def get_last_repository():
    return {'id' : 1, 'full_name' : 'adrianpietka/langs'}

def add_repository(repository):
    print('Insert repository #{} to DB'.format(repository['id']))

def request_get(url):
    response = requests.get(url)

    if (response.status_code != 200):
        raise Exception('Invalid response. Status code: {}'.format(response.status_code))

    return response

def get_repositories(last_repository_id):
    return request_get('https://api.github.com/repositories?since={}'.format(last_repository_id)).json()

def get_repository_metadata(full_name):
    return request_get('https://api.github.com/repos/{}'.format(full_name)).json()
    
def github_sync_repositories():
    print('Sync new repositories from GitHub')
    last_repository = get_last_repository()
    repositories = get_repositories(last_repository['id'])
    for repository in repositories:
        print('Repo #{}: {}'.format(repository['id'], repository['full_name']))
        add_repository(repository)
        
def github_sync_metadata():
    print('Sync metadata for new repositories of GitHub')
    repository = get_last_repository()
    metadata = get_repository_metadata(repository['full_name'])
    for key in metadata:
        print('{} : {}'.format(key, metadata[key]))
