from os import environ

config = {
    'db_host' : environ.get('DB_HOST', 'localhost'),
    'db_user' : environ.get('DB_USER', 'root'),
    'db_password' : environ.get('DB_PASSWORD', ''),
    'db_database' : environ.get('DB_DATABASE', 'fod'),
    'db_charset' : environ.get('DB_CHARSET', 'utf8'),

    'github_username' : environ.get('GITHUB_USERNAME', ''),
    'github_password' : environ.get('GITHUB_PASSWORD', '')
}