import pandas as pd
import os
from loguru import logger

# print(os.listdir())
path = 'HomeC.csv'
df = pd.read_csv(path)
# print(df)


ln = 43_800*2
dfs = []
time_sequence = None

for i in range(5):
    start_index = ln*i
    end_index = ln*(i+1)-1 # inclusive
    logger.debug((start_index, end_index))
    temp_df = df.loc[start_index:end_index,:].copy()
    dfs.append(temp_df)
    logger.debug(temp_df.shape)

    if time_sequence is None:
        time_sequence = list(dfs[0].time)
    else:
        temp_df['time'] = time_sequence

    # logger.debug(temp_df['time'])
    temp_df.to_csv(f'user_{i}_df.csv')
