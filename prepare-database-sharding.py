import pymysql.cursors
from config import config
from string import ascii_lowercase

if not __name__ == '__main__':
    print('Unsupported execution type.')
    sys.exit(0)

try:
    db = pymysql.connect(host=config['db_host'], user=config['db_user'], password=config['db_password'], 
        db=config['db_database'], charset=config['db_charset'], cursorclass=pymysql.cursors.DictCursor)

    shards = 'abcdef0123456789'
    sql_drop_table = ('DROP TABLE IF EXISTS `github_index_{}`')
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

    for shard in shards:
        with db.cursor() as cursor:
            cursor.execute(sql_drop_table.format(shard))
            cursor.execute(sql_create_table.format(shard))
            cursor.execute(sql_move_rows.format(shard, shard))
            db.commit();
            print('Complete: github_index_{}'.format(shard))
    print('Finished.')
finally:
    db.close()