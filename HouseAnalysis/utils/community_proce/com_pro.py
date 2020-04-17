import re
import numpy as np
import pandas as pd

from sqlalchemy import create_engine

import sys

sys.path.insert(0, '../../')

import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'HouseAnalysis.settings'

import django

django.setup()

from house.models import Community, CommunityRange, Region

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house')
df_sql = 'select community_name, region, unit_price, lng, lat from house_api'
df = pd.read_sql(df_sql, engine)
df['region'] = df['region'].apply(lambda x: re.sub(r"\[|\]|'", '', x).split(',')[0])

region = df['region'].value_counts().index

ranges = []
flag = 0
for i in range(1,100):
    if i <= 10:
        ranges.append({
            'priceRange': i,
            'min': flag,
            'max': flag + 4000
          })
        flag = flag + 4000
    else :
        ranges.append({
            'priceRange': i,
            'min': flag,
            'max': flag + 5000
          })
        flag = flag + 5000
    if flag > 95000:
        break

def judgePriceRange(price):
    RANG = filter(lambda item: price >= item['min'] and price < item['max'], ranges)
    return next(RANG)['priceRange']

for reg in region:
    mean_prices = []
    communities = []
    community = df[df['region']==reg]['community_name'].value_counts().index
    community_num = df[df['region']==reg]['community_name'].value_counts().values

    for comm,num in zip(community,community_num):
        lng = df[df['community_name']==comm]['lng'].iloc[0]
        lat = df[df['community_name']==comm]['lat'].iloc[0]

        mean_price = df[df['region'] == reg][df['community_name'] == comm]['unit_price'].mean()
        mean_price = float(format(mean_price, '.3f'))
        rangeIndex = judgePriceRange(mean_price)

        mean_prices.append(mean_price)
        communities.append(comm)

        CommunityModel = Community()
        RegionModel = Region.objects.filter(region=reg)
        CommunityModel.version = 'v1'
        CommunityModel.title = '小区信息'
        CommunityModel.region = RegionModel[0]
        CommunityModel.name = comm
        CommunityModel.num = num
        CommunityModel.mean_unit_price = mean_price
        CommunityModel.rangeIndex = rangeIndex
        CommunityModel.lng = lng
        CommunityModel.lat = lat
        CommunityModel.save()

    print(reg+'community执行完成')

    mean_prices = np.array(mean_prices)
    # 降序排列,取前10个元素
    max_ten_price = np.sort(mean_prices)[::-1][0:10]
    max_ten_price_index = np.argsort(-mean_prices)[0:10]
    max_ten_communities = np.array(communities)[max_ten_price_index]

    for i in range(10):
        CommunityRangeModel = CommunityRange()
        RegionModel = Region.objects.filter(region=reg)
        CommunityRangeModel.version = 'v1'
        CommunityRangeModel.title = '小区信息'
        CommunityRangeModel.region = RegionModel[0]
        CommunityRangeModel.name = max_ten_communities[i]
        CommunityRangeModel.mean_unit_price = max_ten_price[i]
        CommunityRangeModel.save()

    print(reg+'community_range执行完成')
