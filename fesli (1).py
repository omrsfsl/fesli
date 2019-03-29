#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import numpy


# In[2]:


def process_file(filename):
    df = pandas.read_csv(filename, delim_whitespace=True)
    boughtarray = numpy.asarray(df['Bought'])
    costarray = numpy.asarray(df['Cost'])
    consumedarray = numpy.asarray(df['Consumed'])
    return boughtarray, costarray, consumedarray


# In[3]:


boughtarray, costarray, consumedarray = process_file("Coffee Consumption.txt")


# In[4]:


len(boughtarray)


# In[5]:


len(consumedarray)


# In[6]:


total = 0


# In[7]:


for i, j, k in zip(boughtarray, consumedarray, costarray):
    total += (i - j) * k


# In[8]:


print(total)

