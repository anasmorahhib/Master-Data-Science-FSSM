#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[6]:


#load file contents
data = pd.read_csv('hubble_data.csv')
#show head data
data.head()


# In[7]:


distance =  data[['distance']].values
velocity =  data.recession_velocity.values
# Create linear regression object
regr = linear_model.LinearRegression()
regr.fit(distance, velocity)
velocity_pred = regr.predict(distance)


# In[8]:


# scatter plot
fig = plt.figure(figsize=(10,7))
plt.title("Linear regression")
plt.style.use(plt.style.available[4])
plt.plot(distance, velocity_pred, label='Linear regression', color="orange")
plt.scatter(distance, velocity, label='Points de données')
plt.legend(loc='lower right');
plt.xlabel("distance")
plt.ylabel("velocity")
plt.show()


# In[ ]:




