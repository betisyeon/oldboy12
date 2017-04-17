#!/usr/bin/env python3.6
# coding=utf-8

"""
功能说明：多级菜单
1、实现省市县3级菜单 实现效果如下：
-------------------------------
1 北京
2 上海
3 香港.... 
$ 1
=>> 
1 朝阳
2 海淀
3 昌平...
$ 3
==>>
1 沙河
2 天通苑
3 回龙观...
==>>
$ 3
Self-Introduction
-------------------------------
2、可依次通过输入数字选择进入各子菜单，并在任何一个菜单通过使用字母b和q实现返回上级菜单和退出当前程序
3、所需知识点：list dict
"""

#from collections import defaultdict

def switch_multi_level_menu():

    city_list = ['北京','上海','广州','深圳']
    district_list = {1:{'北京':{1:{'朝阳区':{1:'国贸',2:'呼家楼',3:'团结湖'}},
                            2:{'海淀区':{1:'上地',2:'苏州街',3:'国图'}},
                            3:{'昌平':{1:'回龙观',2:'沙河',3:'十三陵'}},
                            4:{'丰台':{1:'方庄',2:'赵公口',3:'木樨园'}}}},
                     2:{'上海':{1:{'浦东新区':{1:'陆家嘴',2:'洋泾',3:'张江'}},
                            2:{'虹口区':{1:'虹口足球场',2:'和平公园',3:'同济大学'}},
                            3:{'徐汇区':{1:'徐家汇',2:'漕河泾',3:'交大'}},
                            4:{'静安区':{1:'静安寺',2:'华山医院',3:'戏剧学院'}}}}}

    while True:

        print("城市列表：")
        for k,v in district_list.items():
            print("%d - %s" % (k,list(v.keys())[0]))
        # input的输出为字符型，需要使用int转换成整型
        city_index = int(input("请输入城市代码："))
        # 从字典中获取"北京"
        city_name = list(district_list[city_index].keys())[0]
        while city_name in city_list:
            # 获取所输入城市的区划字典
            district_dict = district_list[city_index][city_name]
            target_district_list = [None]
            print(district_dict)
            print("%s的行政区划列表：" % city_name)
            # 获取隶属于"北京"的行政区划列表
            for k,v in district_dict.items():
                print("%d - %s" % (k, list(v.keys())[0]))
                target_district_list.append(list(v.keys())[0])
            # 用户输入行政区划代码并将字符型转换为整型
            district_index = int(input("请输入当前行政区划代码："))
            # 获取当前输入的行政区划名称
            district_name = list(district_dict[district_index].keys())[0]

            while district_name in target_district_list:
                print("%s的地标列表：" % district_name)
                # 获取当前行政区划内的地标字典，即列表
                place_dict = district_dict[district_index][district_name]
                # 按顺序显示当前区划内的地标列表
                for k,v in place_dict.items():
                    print("%d - %s" % (k, v))
                # 用户输入当前关注的地标代码
                place_index = int(input("请输入当前地标的代码："))
                # 获取当前地标的名称
                place_name = place_dict[place_index]
                if place_name in place_dict.values():
                    # 提示用户当前所选择地标的具体位置
                    print("您当前所选地标为: %s市-%s-%s" % (city_name,district_name,place_name))
                else:
                    pass
        else:
            print("输入有误，请重新输入！")



    #print(district_list.get(1).get("北京").get(2).get("海淀区").get(2))
    # d = sorted([k for k in district_list.keys()])
    # print(d)
    # print("城市列表")
    # for k in d:
    #     print("%d - %s" % (k, district_list[k].keys()))

# city_list = ['北京','上海','广州','深圳']
    # bj_district_list = {'北京':{'朝阳区':['国贸','呼家楼','团结湖'],
    #                           '海淀区':['上地','苏州街','国图'],
    #                           '昌平':['回龙观','沙河','十三陵'],
    #                           '丰台':['方庄','赵公口','木樨园']}}
    # sh_district_list = {'上海':{'浦东新区':['陆家嘴','洋泾','张江'],
    #                           '虹口区':['虹口足球场','和平公园','同济大学'],
    #                           '徐汇区':['徐家汇','漕河泾','交大'],
    #                           '静安区':['静安寺','华山医院','戏剧学院']}}
    # city_index = None
    # district_index = None
    # place_index = None
    #
    # city_list = {1:'北京', 2:'上海', 3:'广州', 4:'深圳'}
    # bj_district_list = {1:'朝阳区',2:'海淀区',3:'昌平区',4:'丰台区'}
    # sh_district_list = {1:'浦东新区',2:'虹口区',3:'徐汇区',4:'静安区'}
    # bj_chaoyang_place_list = {1:'国贸',2:'呼家楼',3:'团结湖'}
    # bj_haidian_place_list = {1:'上地',2:'苏州街',3:'国图'}
    # bj_changping_place_list = {1:'回龙观',2:'沙河',3:'十三陵'}
    # bj_fengtai_place_list = {1:'方庄',2:'赵公口',3:'木樨园'}
    # sh_pudong_place_list = {1:'陆家嘴',2:'洋泾',3:'张江'}
    # sh_hongkou_place_list = {1:'虹口足球场',2:'和平公园',3:'同济大学'}
    # sh_xuhui_place_list = {1:'徐家汇',2:'漕河泾',3:'交大'}
    # sh_jingan_place_list = {1:'静安寺',2:'华山医院',3:'戏剧学院'}
    #
    # #while True:
    # print("城市列表：")
    # for k,v in city_list.items():
    #     print("%d - %s" % (k,v))
    # city_index = input("请输入城市编号（1-%d的整数）：" % city_list.__len__())
    # if city_index < 1 or city_index > 4:
    #     print("输入无效城市编号，请重新输入：")
    #     city_index = input("请输入城市编号（1-%d的整数）：" % city_list.__len__())
    # else:
    #     pass

switch_multi_level_menu()
