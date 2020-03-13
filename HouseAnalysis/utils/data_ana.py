# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

from utils.dataProcessing import single, multiple

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house')

"""
电梯特征
"""
elevator_sql = '''
      select unit_price, price, elevator from house_api;
      '''

# elevator_df = pd.read_sql_query(elevator_sql, engine)
# has_el_num = elevator_df[elevator_df['elevator'] == '有'].shape[0]
# has_mean_price = elevator_df[elevator_df['elevator'] == '有']['price'].mean()
# has_mean_price = format(has_mean_price,'.3f')
# has_mean_unit_price = elevator_df[elevator_df['elevator'] == '有']['unit_price'].mean()
# has_mean_unit_price = format(has_mean_unit_price,'.3f')
# no_el_num = elevator_df[elevator_df['elevator'] == '无'].shape[0]
# no_mean_price = elevator_df[elevator_df['elevator'] == '无']['price'].mean()
# no_mean_price = format(no_mean_price,'.3f')
# no_mean_unit_price = elevator_df[elevator_df['elevator'] == '无']['unit_price'].mean()
# no_mean_unit_price = format(no_mean_unit_price,'.3f')
# data = {
#     "has_el_num":has_el_num,
#     "no_el_num":no_el_num,
#     "has_mean_price":has_mean_price,
#     "has_mean_unit_price":has_mean_unit_price,
#     "no_mean_price":no_mean_price,
#     "no_mean_unit_price":no_mean_unit_price
# }
# # print(son.dumps(data,sort_keys=True))

floor_sql = '''
    select floor from house_api
'''
# floor_df = pd.read_sql(floor_sql, engine)
# floor_df[floor_df['floor']=='暂无数据'] = '18'
# floor_df['floor'] = floor_df['floor'].astype(str)
# floor_df['floor'] = floor_df['floor'].apply(lambda x: re.findall('\d+',x)[0])
# floor_res = floor_df['floor'].value_counts()
# index = floor_res.index #楼层
# values = floor_res.values # 对应房源数
# for inx,val in zip(index,values):
#     print(inx,val)

layout_sql = '''
    select type from house_api
'''
# layout_df = pd.read_sql(layout_sql, engine)
# layout_df['type'] = layout_df['type'].astype(str)
# floor_res = layout_df['type'].value_counts()
# index = floor_res.index # 户型
# values = floor_res.values # 数量
# for inx,val in zip(index,values):
#     print(inx,val)

region_sql = '''
    select region,unit_price,price from house_api
'''
# region_df = pd.read_sql(region_sql, engine)
# region_df['region'] = region_df['region'].astype(str)
# # 只保留市区县
# region_df['region'] = region_df['region'].apply(lambda x:re.sub(r"\[|\]|'",'',x).split(',')[0])
# floor_res = region_df['region'].value_counts()
# index = floor_res.index # 区划
# values = floor_res.values # 数量
# price_mean = 0
# unitprice_mean = 0
# for inx,val in zip(index,values):
#     price_mean = region_df[region_df['region']==inx]['price'].astype(float).mean()
#     unitprice_mean = region_df[region_df['region']==inx]['unit_price'].astype(float).mean()
#     print(inx,val,price_mean,unitprice_mean)

decoration_sql = '''
    select decoration,unit_price,price from house_api
'''
# decoration = pd.read_sql(decoration_sql, engine)
# decoration['decoration'] = decoration['decoration'].astype(str)
# floor_res = decoration['decoration'].value_counts()
# index = floor_res.index # 装修
# values = floor_res.values # 数量
# price_mean = 0
# unitprice_mean = 0
# for inx,val in zip(index,values):
#     price_mean = decoration[decoration['decoration']==inx]['price'].astype(float).mean()
#     unitprice_mean = decoration[decoration['decoration']==inx]['unit_price'].astype(float).mean()
#     print(inx,val,price_mean,unitprice_mean)

purposes_sql = '''
    select purposes from house_api
'''
# purposes_df = pd.read_sql(purposes_sql, engine)
# purposes_df['purposes'] = purposes_df['purposes'].astype(str)
# purposes_df = purposes_df['purposes'].value_counts()
# index = purposes_df.index # 用途
# values = purposes_df.values # 数量
# for inx,val in zip(index,values):
#     print(inx,val)

orientation_sql = '''
    select orientation from house_api
'''
# orientation_df = pd.read_sql(orientation_sql, engine)
# orientation_df['orientation'] = orientation_df['orientation'].astype(str)
# orientation_df = orientation_df['orientation'].value_counts()
# index = orientation_df.index # 朝向
# values = orientation_df.values # 数量
# for inx,val in zip(index,values):
#     print(inx,val)

constructure_sql = '''
    select house_structure from house_api
'''
# constructure_df = pd.read_sql(constructure_sql, engine)
# constructure_df['house_structure'] = constructure_df['house_structure'].astype(str)
# constructure_df = constructure_df['house_structure'].value_counts()
# index = constructure_df.index # 建筑类型
# values = constructure_df.values # 数量
# for inx,val in zip(index,values):
#     print(inx,val)