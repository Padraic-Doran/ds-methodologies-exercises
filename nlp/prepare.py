#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

import acquire


# In[2]:


def normalize(string):
    return unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore') 


# In[3]:


def remove_special_characters(string):
    return re.sub(r"[^a-z0-9'\s]", '', string)


# In[ ]:





# In[4]:


def basic_clean(string):
    """
    Lowercase the string
    Normalize unicode characters
    Replace anything that is not a letter, number, whitespace or a single quote.
    """
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    # remove anything not a space character, an apostrophy, letter, or number
    string = re.sub(r"[^a-z0-9'\s]", '', string)

    # convert newlines and tabs to a single space
    string = re.sub(r'[\r|\n|\r\n]+', ' ', string)
    
    string = string.strip()
    return string


# In[5]:


def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(string, return_str=True)


# In[6]:


def stem(string):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in string.split()]
    string_of_stems = ' '.join(stems)
    return string_of_stems 


# In[7]:


def lemmatize(string):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    string_of_lemmas = ' '.join(lemmas)
    return string_of_lemmas


# In[8]:


def prep_articles(df):
    df["original"] = df.body
    df["stemmed"] = df.body.apply(basic_clean).apply(stem)
    df["lemmatized"] = df.body.apply(basic_clean).apply(lemmatize)
    df["clean"] = df.body.apply(basic_clean).apply(remove_stopwords)
    df.drop(columns=["body"], inplace=True)
    return df


# In[9]:


def prep_blog_posts():
    df = acquire.get_blog_posts()
    return prep_articles(df)


# In[10]:


def prep_news_articles():
    df = acquire.get_news_articles()
    return prep_articles(df)


# In[11]:


def prep_corpus():
    blog_df = prep_blog_posts()
    blog_df["source"] = "Codeup Blog"

    news_df = prep_news_articles()
    news_df["source"] = "InShorts News"

    return blog_df, news_df


# In[12]:


news_df.head()


# In[ ]:




