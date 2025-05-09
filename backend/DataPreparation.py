import pandas as pd
import numpy as np 

def process(df):
    #column ordering
    sorted_columns = sorted(df.columns)
    df=df[sorted_columns]
    
    # Object columns exclusion (only contains meta data)
    df_meta=df.select_dtypes(include=['object'])
    df.drop(columns = list(df_meta.columns) + ['Minimum/Image-original/diagnostics'], inplace=True)

    print('CHECKPOINT 1: ', df.index)
    for col in df.columns:
        
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 6 * IQR
        upper_bound = Q3 + 6 * IQR

        # Reeplace outliers by limits (capping)
        df[col] = df[col].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))
    print('CHECKPOINT 2: ', df.shape)
    return df
