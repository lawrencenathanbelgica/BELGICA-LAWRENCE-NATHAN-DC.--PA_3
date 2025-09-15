#!/usr/bin/env python
# coding: utf-8

# ### PROBLEM 2: Save your file as Surname_Pandas-P2.py
# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
# indexing operations.
# 

# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

# In[1]:


# To access Pandas Library, the import convention must be used
import pandas as pd
cars = pd.read_csv('cars.csv')


# In[7]:


# show the first 5 rows with only the odd-numbered columns (1, 3, 5, …)
cars.iloc[:5, ::2]


# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[8]:


# gets the whole row of data where the Model is exactly 'Mazda RX4'
cars.loc[cars['Model']=='Mazda RX4']


# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[3]:


# gets only the 'cyl' (cylinders) column for the car model 'Camaro Z28'
cars.loc[cars['Model']=='Camaro Z28', ['cyl']]


# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
# 

# In[5]:


# makes a list of models and then shows their 'cyl' (cylinders) and 'gear' values
cars_model = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(cars_model), ['cyl', 'gear']]

