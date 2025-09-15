#!/usr/bin/env python
# coding: utf-8

# In[5]:


# To access Pandas Library, the import convention must be used
import pandas as pd 
cars = pd.read_csv('cars.csv')


# In[7]:


# set as default (first 5 on the list)
cars.head() 


# In[6]:


# set as default (last 5)
cars.tail()

