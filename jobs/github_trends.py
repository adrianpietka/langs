import requests

def get_last_repository():
    return {'id' : 1}

def request_get(url):
    response = requests.get(url)

    if (response.status_code != 200):
        raise Exception('Invalid response. Status code: {}'.format(response.status_code))

    return response

def get_repositories(last_repository_id):
    return request_get('https://api.github.com/repositories?since={}'.format(last_repository_id)).json()

last_repository = get_last_repository()
repositories = get_repositories(last_repository['id'])
for repo in repositories:
    print('Repo #{}: {}'.format(repo['id'], repo['full_name']))