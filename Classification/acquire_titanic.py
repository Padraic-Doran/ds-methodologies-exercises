
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import env
from scipy import stats
import csv
from os import path


def get_db_url(db):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

    
def write_csv_of__titanic_data():
    df = get_zillow_data()
    df.to_csv("./titanic_db.csv")

def read_csv_of_data():
    return 

def get_titanic_data_from_mysql():
   
    # Use a double "%" in order to escape %'s default string formatting behavior.
    query = '''select * from passengers;
    '''

    url = get_url("titanic_db") 
    df = pd.read_sql(query, url)
    return df

def get_titanic_data():
    """
        reads from .csv or issues slq query, writes that sql as a .csv, and returns the data.
    """
    filename = "./titanic_db.csv"
    if path.exists(filename):
        print(f'Reading data from {filename}')
    else:
        print(f'Reading data from query, writing to {filename}, and returning the dataframe')
        write_csv_of_data()

    # Return the dataframe read from the csv
    return pd.read_csv(filename)

# def clean_titanic_data(df):
#     df = df.dropna()
#     df = df[df.bathroom_count > 0]
#     df = df[df.bedroom_count > 0]
#     return df


# def wrangle_titanic():
#     df = get_titanic_data()
#     df = clean_data(df)
#     return df

