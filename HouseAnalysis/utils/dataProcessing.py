# -*- coding: utf-8 -*-
import pandas as pd
import re

def single(sql,engine,feature):
    """
    单因子分析
    :param sql: sql语句
    :param engine: mysql引擎
    :param feature: 数据特征
    :return: 特征，数量
    """
    df_sql = sql
    df = pd.read_sql(df_sql, engine)
    df[feature] = df[feature].astype(str)
    if feature=='floor':
        df[df[feature]=='暂无数据'] = '18'
        df[feature] = df[feature].apply(lambda x: re.findall('\d+',x)[0])
    feature_res = df[feature].value_counts()
    index = feature_res.index
    values = feature_res.values
    return index,values

def multiple(sql,engine,feature):
    """
    多因子分析
    :param sql: sql语句
    :param engine: mysql引擎
    :param feature: 数据特征
    :return: 特征，数量，总价均价，单价均价
    """
    df_sql = sql
    df = pd.read_sql(df_sql, engine)
    df[feature] = df[feature].astype(str)
    if feature == 'region':
        df[feature] = df[feature].apply(lambda x:re.sub(r"\[|\]|'",'',x).split(',')[0])
    feature_res = df[feature].value_counts()
    index = feature_res.index
    values = feature_res.values
    price_mean = []
    unit_price_mean = []
    for inx,val in zip(index,values):
        price_mean.append(format(df[df[feature]==inx]['price'].astype(float).mean(),'.3f'))
        unit_price_mean.append(format(df[df[feature]==inx]['unit_price'].astype(float).mean(),'.3f'))
    return index, values, price_mean, unit_price_mean