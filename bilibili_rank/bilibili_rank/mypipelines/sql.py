import mysql.connector
from bilibili_rank import settings


MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)
class Sql:
    @classmethod
    def creat_table(cls, tables_name):
        sql_drow = 'DROP TABLE IF EXISTS {0};'.format(tables_name)

        sql_creat = 'CREATE TABLE {0}(' \
                    'id int(11) NOT NULL AUTO_INCREMENT ,' \
                    'aid varchar(255) default null,' \
                    'author varchar(255) DEFAULT NULL,' \
                    'coins varchar(255) DEFAULT NULL,' \
                    'duration varchar(255) DEFAULT NULL,' \
                    'm_id varchar(255) DEFAULT NULL,' \
                    'play varchar(255) default null,' \
                    'pts varchar(255) default null,' \
                    'title varchar(255) default null,' \
                    'video_review varchar(255) default null,' \
                    'video_url varchar(255) default null,' \
                    'times varchar(255) default null,' \
                    'menu varchar(255) default null,' \
                    'catalogy varchar(255) default null,' \
                    'PRIMARY KEY (id)) ' \
                    'ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 collate=utf8mb4_unicode_ci;'.format(tables_name)
        # value = {'tables_name': tables_name}
        # print('进入sql.creat')
        # print('table')
        cur.execute(sql_drow)
        cur.execute(sql_creat)

    @classmethod
    def insert_bilibili_name(cls, aid, author, coins, duration, m_id, play, pts, title, video_review, video_url, times, menu, catalogy, tables_name):
        sql = 'INSERT INTO {0} (aid, author, coins, duration, m_id, play, pts, title, video_review, video_url, times, menu, catalogy) ' \
              'VALUES ' \
              '(%(aid)s, %(author)s, %(coins)s, %(duration)s,%(m_id)s, %(play)s,' \
              ' %(pts)s, %(title)s, %(video_review)s, %(video_url)s, %(times)s, %(menu)s, %(catalogy)s)'.format(tables_name)
        value = {
            'aid': aid,
            'author': author,
            'coins': coins,
            'duration': duration,
            'm_id': m_id,
            'play': play,
            'pts': pts,
            'title': title,
            'video_review': video_review,
            'video_url': video_url,
            'times': times,
            'menu': menu,
            'catalogy': catalogy
        }
        # print('进入sql.insert')

        cur.execute(sql, value)
        # cnx.commit()

    @classmethod
    def commit_db(cls):
        # print('进入sql.commit')
        cnx.commit()

