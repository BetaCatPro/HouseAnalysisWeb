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

from house.models import Community, CommunityRange

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house')
df_sql = 'select community_name, region, unit_price from house_api'
df = pd.read_sql(df_sql, engine)
df['region'] = df['region'].apply(lambda x:re.sub(r"\[|\]|'",'',x).split(',')[0])

region = df['region'].value_counts().index

foreignkey = 1
for reg in region:
    mean_prices = []
    communities = []
    community = df[df['region']==reg]['community_name'].value_counts().index

    for comm in community:
        mean_price = df[df['region'] == reg][df['community_name'] == comm]['unit_price'].mean()
        mean_price = float(format(mean_price, '.3f'))
        # Community = Community()
        # Community.version = 'v1'
        # Community.title = '小区信息'
        # Community.region = foreignkey
        # Community.name = comm
        # Community.mean_unit_price = mean_price
        # Community.save()
        mean_prices.append(mean_price)
        communities.append(comm)

    mean_prices = np.array(mean_prices)
    # 降序排列,取前10个元素
    max_ten_price = np.sort(mean_prices)[::-1][0:10]
    max_ten_price_index = np.argsort(-mean_prices)[0:10]
    max_ten_communities = np.array(communities)[max_ten_price_index]

    for i in range(10):
        CommunityRange = CommunityRange()
        CommunityRange.version = 'v1'
        CommunityRange.title = '小区信息'
        CommunityRange.region = foreignkey
        CommunityRange.name = max_ten_communities[i]
        CommunityRange.mean_unit_price = mean_prices[i]
        CommunityRange.save()

    foreignkey = foreignkey + 1



