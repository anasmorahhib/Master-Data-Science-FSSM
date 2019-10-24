#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[2]:


# load the file contents
data = pd.read_csv('hubble_data.csv')
# show data
data.head()


# In[3]:


# Create distance & velocity variables
distance =  data[['distance']].values
velocity =  data.recession_velocity.values


# In[4]:


# Plot data
fig = plt.figure(figsize=(10,7))
plt.title("Scatter plot: ubble Data")
plt.style.use(plt.style.available[4])
plt.scatter(distance, velocity, label='Data points')
plt.legend(loc='lower right');
plt.xlabel("distance")
plt.ylabel("velocity")
plt.show()


# In[5]:


# Create linear regression object between distance & velocity
regr = linear_model.LinearRegression()
regr.fit(distance, velocity)
velocity_pred = regr.predict(distance)


# In[6]:



fig = plt.figure(figsize=(10,7))
plt.title("Hubble data / linear regression on data")
plt.style.use(plt.style.available[4])
plt.plot(distance, velocity_pred, label='linear regression', color="orange")
plt.scatter(distance, velocity, label='Data points')
plt.legend(loc='lower right');
plt.xlabel("distance")
plt.ylabel("velocity")
plt.show()

