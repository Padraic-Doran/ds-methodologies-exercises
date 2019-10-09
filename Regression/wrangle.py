#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from env import user, host, password
from scipy import stats
import csv

np.random.seed(29)


# In[12]:


def get_db_url(username, hostname, password, db_name):
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

query = '''
   Select `customer_id`, monthly_charges, `total_charges`, tenure from customers
Where contract_type_id = 3
;
'''

url = get_db_url(user,host,password,'telco_churn')
charges = pd.read_sql(query,url)
charges.head()


# In[13]:


charges.info()


# In[21]:


charges.total_charges.value_counts(sort=True, ascending=False)


# In[24]:


charges.total_charges.replace(r'^\s*$', np.nan, regex=True, inplace=True)


# In[25]:


charges.info()


# In[27]:


charges = charges.dropna()


# In[32]:


charges.total_charges = charges.total_charges.astype(float)
charges.total_charges
charges.info()


# In[33]:


def wrangle_telco():
    query = '''
       Select `customer_id`, monthly_charges, `total_charges`, tenure from customers
    Where contract_type_id = 3
    ;
    '''

    url = get_db_url(user,host,password,'telco_churn')
    charges = pd.read_sql(query,url)
    charges.total_charges.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    charges = charges.dropna()
    charges.total_charges = charges.total_charges.astype(float)
    return charges


# In[34]:





# In[ ]:




