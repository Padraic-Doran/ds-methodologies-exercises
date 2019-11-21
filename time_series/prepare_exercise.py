#!/usr/bin/env python
# coding: utf-8

# In[6]:


import acquire
import pandas as pd
import numpy as np


# In[9]:


acquire.get_all_data()


# In[12]:


import pandas as pd

def prep_store_data(df):
    # parse the date column and set it as the index
    fmt = '%a, %d %b %Y %H:%M:%S %Z'
    df.sale_date = pd.to_datetime(df.sale_date, format=fmt)
    df = df.sort_values(by='sale_date').set_index('sale_date')

    # add some time components as features
    df['month'] = df.index.strftime('%m-%b')
    df['weekday'] = df.index.strftime('%w-%a')

    # derive the total sales
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

def get_sales_by_day(df):
    sales_by_day = df.resample('D')[['sales_total']].sum()
    sales_by_day['diff_with_last_day'] = sales_by_day.sales_total.diff()
    return sales_by_day


# In[ ]:




