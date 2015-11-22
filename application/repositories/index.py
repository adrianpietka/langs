from datetime import datetime

class IndexRepository:
    def __init__(self, db):
        self.db = db

    def _convert_date_time(self, value):
        try:
            dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
            return dt.__format__('%Y-%m-%d %H:%M:%S')
        except:
            return value

    def get_last_repository_id(self):
        with self.db.cursor() as cursor:
            cursor.execute('SELECT id FROM github_index ORDER BY id DESC LIMIT 1')
            result = cursor.fetchone()
            return result['id'] if result != None else 0

    def get_repository_to_update_metadata(self, limit):
        with self.db.cursor() as cursor:
            cursor.execute('SELECT id, full_name FROM github_index ORDER BY metadata_updated_at ASC, id ASC LIMIT %s', (limit))
            return cursor.fetchall()

    def add_repository(self, repository):
        sql = 'INSERT INTO github_index (id, full_name, owner_login, description) VALUES(%s, %s, %s, %s)'
        with self.db.cursor() as cursor:
            values = (int(repository['id']), repository['full_name'], repository['owner']['login'], repository['description'])
            cursor.execute(sql, values)
        self.db.commit()

    def update_repository_metadata(self, id, metadata):
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
        with self.db.cursor() as cursor:
            values = (self._convert_date_time(metadata['created_at']), self._convert_date_time(metadata['pushed_at']),
                metadata['language'], metadata['stargazers_count'],
                metadata['watchers_count'], metadata['forks_count'],
                metadata['network_count'], id)
            cursor.execute(sql, values)
        self.db.commit();

    def omit_repository_metadata(self, id):
        metadata = {
            'created_at' : None,
            'pushed_at' : None,
            'language' : None,
            'stargazers_count' : None,
            'watchers_count' : None,
            'forks_count' : None,
            'network_count' : None
        }
        self.update_repository_metadata(id, metadata)

    def get_processed_repositories_number(self):
        sql = ('SELECT COUNT(*) AS total '
            'FROM github_index '
            'WHERE metadata_updated_at IS NOT NULL')
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['total']

    def get_repositories_number(self):
        sql = ('SELECT COUNT(*) AS total '
            'FROM github_index')
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['total']

    def get_oldest_repository(self):
        sql = ('SELECT full_name, created_at '
            'FROM github_index '
            'WHERE created_at IS NOT NULL '
            'ORDER BY created_at ASC')
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            return dict(name=result['full_name'], created=result['created_at'].isoformat())

    def get_latest_repository(self):
        sql = ('SELECT full_name, created_at '
            'FROM github_index '
            'WHERE created_at IS NOT NULL '
            'ORDER BY created_at DESC')
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            return dict(name=result['full_name'], created=result['created_at'].isoformat())

    def get_all_languages(self):
        sql = ('SELECT DISTINCT(language) AS `language`'
            'FROM github_index '
            'WHERE language IS NOT NULL ')
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            return [row['language'] for row in cursor.fetchall()]

    def get_languages_stats(self):
        sql = ('SELECT language, COUNT(*) AS `repositories`'
            'FROM github_index '
            'WHERE language IS NOT NULL '
            'GROUP BY language '
            'ORDER BY COUNT(*) DESC')
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def new_repositories_monthly(self):
        sql = ('SELECT language, DATE_FORMAT(created_at, \'%Y-%m\') AS `created`, COUNT(*) AS `count` '
            'FROM github_index '
            'WHERE language IN (\'Ruby\', \'JavaScript\', \'PHP\', \'Python\', \'Perl\', \'C\') '
            'GROUP BY language, DATE_FORMAT(created_at, \'%Y-%m\') '
            'ORDER BY DATE(created_at) DESC')
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            aggregated = {}
            for item in cursor.fetchall():
                if not item['language'] in aggregated:
                    aggregated[item['language']] = {}
                aggregated[item['language']][item['created']] = item['count']
            return aggregated

    def new_repositories_yearly(self):
        sql = ('SELECT language, YEAR(created_at) AS `created`, COUNT(*) AS `count` '
            'FROM github_index '
            'WHERE language IN (\'Ruby\', \'JavaScript\', \'PHP\', \'Python\', \'Perl\', \'C\') '
            'GROUP BY language, YEAR(created_at) '
            'ORDER BY DATE(created_at) DESC')
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            aggregated = {}
            for item in cursor.fetchall():
                if not item['language'] in aggregated:
                    aggregated[item['language']] = {}
                aggregated[item['language']][item['created']] = item['count']
            return aggregated