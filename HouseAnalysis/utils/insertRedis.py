# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, '../')

import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'HouseAnalysis.settings'

import django
from django.db.models import Avg

django.setup()

from house.models import Api

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='', db=4)
redis_conn = redis.Redis(connection_pool=redis_pool)

house = Api.objects.all()
all_number = house.count()
com_number = Api.objects.values('community_name').distinct().count()
mean_price = format(house.aggregate(Avg('price'))['price__avg'],'.3f')
mean_unit_price = format(house.aggregate(Avg('unit_price'))['unit_price__avg'],'.3f')
data = {
    "all_number": all_number,
    "com_number": com_number,
    "mean_price": mean_price,
    "mean_unit_price": mean_unit_price
}

redis_conn.mset(data)
