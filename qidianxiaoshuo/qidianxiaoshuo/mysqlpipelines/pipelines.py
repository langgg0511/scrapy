from .sql import Sql
from qidianxiaoshuo.items import QidianxiaoshuoItem

class QidianxiaoshuoPipeline(object):

    def process_item(self, item, spider):
        # deferToThread(self._process_item, item, spider)
        if isinstance(item, QidianxiaoshuoItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print('已经存在该小说')
                pass
            else:
                xs_name = item['name']
                xs_author = item['author']
                category = item['category']
                statue = item['statue']
                tag = item['tag']
                xs_number = item['number']
                info = item['info']
                xs_url = item['novel_url']
                Sql.insert_dd_name(xs_name, xs_author, category, name_id, statue, tag, xs_number, info, xs_url)
                print('开始存《%s》数据进入数据库' %xs_name)




