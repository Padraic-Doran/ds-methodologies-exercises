#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def get_the_data():
    '''
    Acquires data from anonymized-curriculum-access.txt
    '''

    df = pd.read_csv('anonymized-curriculum-access.txt', sep=' ', header=None, engine='python')
    
    return df

