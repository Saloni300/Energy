import os
from loguru import logger
import pandas as pd
import random
import json
from enum import Enum
from uuid import uuid4

from pymongo import MongoClient
from pymongo.collection import Collection


# user ids => user_0, user_1, user_2, user_3, user_4

files = ['user_0_df.csv', 'user_1_df.csv', 'user_2_df.csv', 'user_3_df.csv', 'user_4_df.csv']

# MONTH_RECORD_LENGTH = 43_800
MONTH_RECORD_LENGTH = 43
MONTHS_COVERED = 2
dfs = []
user_data = {}

# dfs => df0, df1, df2, df3, df4
for file in files:
    df = pd.read_csv(file)
    # 2 month record
    dfs.append(df)
    # time_index = pd.date_range('2016-01-01 05:00', periods=len(df),  freq='min')  
    # time_index = pd.date_range('%Y-%m-%d %H:%M:%S', periods=len(df),  freq='min')  
    # time_index = pd.DatetimeIndex(time_index)
    # df = df.set_index(time_index)
    pd.to_datetime(df['time'], unit = 's')
    logger.debug(df)
    # df = df.drop(['time'], axis=1)
    df.columns = [col.replace(' [kW]', '') for col in df.columns]
    # logger.debug('chk')
    consumption_mean = df['use'].mean()   # mu
    consumption_standard_deviation = df['use'].std() # sigma
    
    # recent month (rm)
    start_index = MONTH_RECORD_LENGTH*0
    end_index = MONTH_RECORD_LENGTH*(0+1)-1 # inclusive
    # df_recent_month = df.loc[start_index:end_index,:]
    df_recent_month = df.loc[start_index:end_index,:].copy()
    consumption_mean_rm = df_recent_month['use'].mean()   # mu
    consumption_standard_deviation_rm = df_recent_month['use'].std() # sigma

    # # previous month (pm)
    start_index = MONTH_RECORD_LENGTH*1
    end_index = MONTH_RECORD_LENGTH*(1+1)-1 # inclusive
    df_previous_month = df.loc[start_index:end_index,:].copy()
    consumption_mean_pm = df_previous_month['use'].mean()   # mu
    consumption_standard_deviation_pm = df_previous_month['use'].std() # sigma
    
    data = {
        'recent_month': {
            'mean_consumption': consumption_mean_rm,
            'standard_deviation': consumption_standard_deviation_rm
        },
        'previous_month': {
            'mean_consumption': consumption_mean_pm,
            'standard_deviation': consumption_standard_deviation_pm
        },
    }
    user_id = file.split('_df')[0]
    user_data[user_id] = data


# write data to mongodb
logger.debug(user_data)


CONNECTION_STRING = "mongodb://database"
DB_NAME = 'energy'
COLLECTION_NAME = 'user-consumption'

def get_collection() -> Collection:
    client = MongoClient(CONNECTION_STRING)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection

collection = get_collection()
collection.insert_one(user_data)

logger.debug(user_data)
