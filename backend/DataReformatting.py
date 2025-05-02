import pandas as pd
import numpy as np 
import ast
import os
import re
from datetime import datetime

inter_dir='processedData'
now = datetime.now()
formattedDate = now.strftime("%Y-%m-%d %H:%M:%S")

# ---------------------------- UTILITIES ----------------------------

def tupleExtraction(df):
    for col in df.columns:
        try: 
            parsed = ast.literal_eval(df[col][0])  # [0] because its a dataframe with 1 row
            if isinstance(parsed, tuple):
                # Extract tuple values and clean them
                vals = [re.sub(r'[()]', '', str(x)) for x in df[col]]  # Convert to strings
                vals = [x.split(',') for x in vals]  

                # Create new DataFrame with the extracted values
                asciiNum = 97  # ASCII 'a'
                temp_df = pd.DataFrame()

                for row_idx, tpl in enumerate(vals):  
                    for i in range(len(tpl)):
                        newAscii = chr(asciiNum + i)  # Convert to letter
                        newCol = f"{newAscii}.{col}"  
                        
                        if newCol not in temp_df.columns:
                            temp_df[newCol] = None  
                        
                        temp_df.loc[row_idx, newCol] = tpl[i]
                        temp_df[newCol]=pd.to_numeric(temp_df[newCol])
                
                df.drop(columns=[col], inplace=True)  
                df = pd.concat([df, temp_df], axis=1)
        except (ValueError, SyntaxError):
            
            pass

    return df


def reformatting(df):
    if not os.path.exists(inter_dir):
        os.makedirs(inter_dir)
    print(df.columns)
    df['Feature Name']=df['Feature Name']+"/"+df['Feature Class']+"/"+df['Image type']
    print(df.shape)
    # only considering columns 'Feature Name' and 'Segment...' as columns and values respectively
    df = df.set_index('Feature Name')
    df.drop(columns=['Image type', 'Feature Class'], inplace=True)

    df_transposed = df.T 
    
    id_col=[col for col in df_transposed.columns if col.startswith("Id/")][0]
    df_transposed.rename(columns={id_col: "Id"}, inplace=True)

    output_file = inter_dir+'/inter.csv'

    df_transposed.to_csv(output_file) #writes processed file



# ---------------------------- MAIN ----------------------------
def process(df):
    finalDf = pd.DataFrame()

  
    reformatting(df) 
    df = pd.read_csv(inter_dir+'/inter.csv') #reads processed file
    
    df=tupleExtraction(df)
    
    finalDf = pd.concat([finalDf, df])
    print('COLUMNS: ', finalDf.columns)
    print('FINAL SHAPE: ', finalDf.shape)    
    return finalDf
