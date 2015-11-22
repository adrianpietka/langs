class PrepareDatabaseSharding:
    shards = 'abcdef0123456789'
    sql_drop_table = 'DROP TABLE IF EXISTS `github_index_{}`'
    sql_create_table = ('CREATE TABLE IF NOT EXISTS `github_index_{}` ( '
        '`id` bigint(20) unsigned NOT NULL, '
        '`full_name` varchar(250) NOT NULL, '
        '`owner_login` varchar(250) NOT NULL, '
        '`description` text, '
        '`metadata_updated_at` datetime DEFAULT NULL, '
        '`created_at` datetime DEFAULT NULL, '
        '`pushed_at` datetime DEFAULT NULL, '
        '`language` varchar(50) DEFAULT NULL, '
        '`stargazers_count` int(11) DEFAULT NULL, '
        '`watchers_count` int(11) DEFAULT NULL, '
        '`forks_count` int(11) DEFAULT NULL, '
        '`network_count` int(11) DEFAULT NULL, '
        'PRIMARY KEY (`id`), '
        'KEY `language` (`language`) '
    ') ENGINE=InnoDB DEFAULT CHARSET=utf8;')
    sql_move_rows = 'INSERT INTO github_index_{} SELECT * FROM github_index WHERE LEFT(MD5(full_name), 1) = \'{}\''

    def __init__(self, db):
        self.db = db

    def execute(self):
        try:
            for shard in self.shards:
                with self.db.cursor() as cursor:
                    cursor.execute(self.sql_drop_table.format(shard))
                    cursor.execute(self.sql_create_table.format(shard))
                    cursor.execute(self.sql_move_rows.format(shard, shard))
                    self.db.commit();
                    print('Complete: github_index_{}'.format(shard))
        finally:
            print('Finished.')