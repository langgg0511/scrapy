from .sql import Sql
from bilibili_rank.items import BilibiliRankItem,BilibiliDictItem

class BilibiliPipeline(object):

    def process_item(self, item, spider):
        # deferToThread(self._process_item, item, spider)
        # print("This is pipeline")
        if isinstance(item, BilibiliDictItem):
            # print('进入pipelines1 将执行creat')
            tables_name = item['tables_name']
            Sql.creat_table(tables_name)
        elif isinstance(item, BilibiliRankItem):
            aid = item['aid']
            author = item['author']
            coins = item['coins']
            duration = item['duration']
            m_id = item['mid']
            play = item['play']
            pts = item['pts']
            title = item['title']
            video_review = item['video_review']
            video_url = item['video_url']
            times = item['times']
            menu = item['menu']
            catalogy = item['catalogy']
            # tables_name2 = menu + '_' + times + '_' + catalogy
            tables_name = item['tables_name']
            # print('进入Pipelines 将执行insert')
            Sql.insert_bilibili_name(aid, author, coins, duration, m_id, play, pts,
                                     title, video_review, video_url, times, menu, catalogy, tables_name)
            # print('insert 执行完成')
            # print(tables_name + "爬取完成")
            Sql.commit_db()
            # return item




