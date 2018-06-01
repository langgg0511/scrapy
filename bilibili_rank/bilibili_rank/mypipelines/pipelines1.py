from .sql import Sql
from bilibili_rank.items import BilibiliDictItem

class BilibiliPipeline1(object):

    def process_item(self, item_list, spider):
        # deferToThread(self._process_item, item, spider)
        print("This is pipeline1")
        if isinstance(item_list, BilibiliDictItem):
            # menu_list = item_list['menu_list']
            # times_list = item_list['times_list']
            # catalogy_list = item_list['catalogy_list']
            # for menu_name in menu_list[0:1]:
            #     for times_name in times_list[0:1]:
            #         for catalogy_name in catalogy_list[0:2]:
            #             tables_name = menu_name+'_'+times_name+'_'+catalogy_name
            #             # tables_name = '{0}_{1}_{2}_name'.format(menu_name, times_name, catalogy_name)
            #             Sql.creat_table(tables_name)
            print('进入pipelines1 将执行creat')
            tables_name = item_list['tables_name']
            Sql.creat_table(tables_name)
            # print('creat 执行完成')
            # yield item_list