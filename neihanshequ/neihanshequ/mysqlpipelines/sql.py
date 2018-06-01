import mysql.connector
from neihanshequ import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB, charset='utf8mb4')
cur = cnx.cursor(buffered=True)
print('数据库已连接！')
class Sql:
    @classmethod
    def insert_dd_name(cls, nh_name, nh_text, digg, bury, nh_comment, nh_share, repin, nh_id):
        sql = 'INSERT INTO dd_name (nh_name, nh_text, digg, bury, nh_comment, nh_share, repin, nh_id) VALUES (%(nh_name)s, %(nh_text)s,%(digg)s,%(bury)s,%(nh_comment)s,%(nh_share)s,%(repin)s,%(nh_id)s)'
        value = {
            'nh_name': nh_name,
            'nh_text': nh_text,
            'digg': digg,
            'bury': bury,
            'nh_comment': nh_comment,
            'nh_share': nh_share,
            'repin': repin,
            'nh_id': nh_id
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def id_name(cls, nh_id):
        sql = 'SELECT id FROM dd_name WHERE nh_id=%(nh_id)s'
        value = {
            'xs_name': nh_id
        }
        cur.execute(sql, value)
        for nh_id in cur:
            return nh_id[0]

    @classmethod
    def select_id(cls, nh_id):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE nh_id=%(nh_id)s)"
        value = {
            'nh_id': nh_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]
