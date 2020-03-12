# -*- coding: utf-8 -*-
import pandas as pd
import json
import re
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house')

"""
电梯特征
"""
elevator_sql = '''
      select unit_price, price, elevator from house_api;
      '''

elevator_df = pd.read_sql_query(elevator_sql, engine)
has_el_num = elevator_df[elevator_df['elevator'] == '有'].shape[0]
has_mean_price = elevator_df[elevator_df['elevator'] == '有']['price'].mean()
has_mean_price = format(has_mean_price,'.3f')
has_mean_unit_price = elevator_df[elevator_df['elevator'] == '有']['unit_price'].mean()
has_mean_unit_price = format(has_mean_unit_price,'.3f')
no_el_num = elevator_df[elevator_df['elevator'] == '无'].shape[0]
no_mean_price = elevator_df[elevator_df['elevator'] == '无']['price'].mean()
no_mean_price = format(no_mean_price,'.3f')
no_mean_unit_price = elevator_df[elevator_df['elevator'] == '无']['unit_price'].mean()
no_mean_unit_price = format(no_mean_unit_price,'.3f')
data = {
    "has_el_num":has_el_num,
    "no_el_num":no_el_num,
    "has_mean_price":has_mean_price,
    "has_mean_unit_price":has_mean_unit_price,
    "no_mean_price":no_mean_price,
    "no_mean_unit_price":no_mean_unit_price
}
# # print(son.dumps(data,sort_keys=True))

floor_sql = '''
    select floor from house_api
'''
floor_df = pd.read_sql(floor_sql, engine)
index = re.findall('\d+',str(floor_df['floor'].value_counts().index.index))
item = floor_df['floor'].value_counts().values