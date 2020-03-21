# -*- coding: utf-8 -*-
from utils.dataProcessing import single, multiple
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house')

import sys

sys.path.insert(0, '../')

import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'HouseAnalysis.settings'

import django

django.setup()

from house.models import Elevator, Floor, Layout, Region, Decortion, Purposes, Orientation, Constructure


class InsertIntoMysql():

    def __init__(self):
        self.elevator_sql = 'select unit_price, price, elevator from house_api'
        self.floor_sql = 'select floor from house_api'
        self.layout_sql = 'select type from house_api'
        self.region_sql = 'select region,unit_price,price from house_api'
        self.decoration_sql = 'select decoration,unit_price,price from house_api'
        self.purposes_sql = 'select purposes from house_api'
        self.orientation_sql = 'select orientation from house_api'
        self.constructure_sql = 'select house_structure from house_api'

    def insertElevator(self):
        index, values, price_mean, unit_price_mean = multiple(self.elevator_sql, engine, 'elevator')
        for i in range(len(index)):
            elevator = Elevator()
            elevator.version = 'v1'
            elevator.title = '电梯分布情况'
            elevator.has_ele = index[i]
            elevator.el_num = values[i]
            elevator.mean_price = price_mean[i]
            elevator.mean_unit_price = unit_price_mean[i]
            elevator.save()

    def insertFloor(self):
        index, values = single(self.floor_sql, engine, 'floor')
        for inx, val in zip(index, values):
            floor = Floor()
            floor.version = 'v1'
            floor.title = '楼层分布情况'
            floor.floor = inx
            floor.num = val
            floor.save()

    def insertType(self):
        index, values = single(self.layout_sql, engine, 'type')
        for inx, val in zip(index, values):
            layout = Layout()
            layout.version = 'v1'
            layout.title = '户型分布情况'
            layout.layout = inx
            layout.num = val
            layout.save()

    def insertRegion(self):
        index, values, price_mean, unit_price_mean, max_unit_price, min_unit_price = multiple(self.region_sql, engine, 'region')
        for i in range(len(index)):
            region = Region()
            region.version = 'v1'
            region.title = '区划分布情况'
            region.region = index[i]
            region.num = values[i]
            region.mean_price = price_mean[i]
            region.mean_unit_price = unit_price_mean[i]
            region.max_unit_price = max_unit_price[i]
            region.min_unit_price = min_unit_price[i]
            region.save()

    def insertDecoration(self):
        index, values, price_mean, unit_price_mean = multiple(self.decoration_sql, engine, 'decoration')
        for i in range(len(index)):
            decoration = Decortion()
            decoration.version = 'v1'
            decoration.title = '装修分布情况'
            decoration.decoration = index[i]
            decoration.num = values[i]
            decoration.mean_price = price_mean[i]
            decoration.mean_unit_price = unit_price_mean[i]
            decoration.save()

    def insertPurposes(self):
        index, values = single(self.purposes_sql, engine, 'purposes')
        for inx, val in zip(index, values):
            purposes = Purposes()
            purposes.version = 'v1'
            purposes.title = '用途分布情况'
            purposes.purposes = inx
            purposes.num = val
            purposes.save()

    def insertOrientation(self):
        index, values = single(self.orientation_sql, engine, 'orientation')
        for inx, val in zip(index, values):
            orientation = Orientation()
            orientation.version = 'v1'
            orientation.title = '朝向分布情况'
            orientation.orientation = inx
            orientation.num = val
            orientation.save()

    def insertStructure(self):
        index, values = single(self.constructure_sql, engine, 'house_structure')
        for inx, val in zip(index, values):
            structure = Constructure()
            structure.version = 'v1'
            structure.title = '建筑结构分布情况'
            structure.constructure = inx
            structure.num = val
            structure.save()

