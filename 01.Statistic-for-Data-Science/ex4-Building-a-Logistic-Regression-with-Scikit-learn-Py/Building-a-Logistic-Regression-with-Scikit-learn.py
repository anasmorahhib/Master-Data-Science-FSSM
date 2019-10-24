#!/usr/bin/env python
# coding: utf-8

# In[135]:


# Building a Logistic Regression in Python


# In[136]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


# In[137]:


data = pd.read_csv('ex2data1.txt', header=None)
data.head(3)


# In[138]:


X = data[[0,1]].values
y = data[2]


# In[139]:


# use LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X, y)


# In[140]:


# Predict class labels for samples in X
log_reg_pred = log_reg.predict(X)
log_reg_pred


# In[141]:


# Probability estimates.
log_reg.predict_proba(X[:10, :]) 


# In[142]:


# Returns the mean accuracy on the given test data and labels.
log_reg.score(X, y)


# In[143]:


# Plot data
fig = plt.figure(figsize=(10,7))
plt.title("Logistic regression")
plt.style.use(plt.style.available[4])
colors=['red' if l==0 else 'blue' for l in y]
plt.scatter(X[:, 0], X[:, 1], label='Logistics regression', color=colors)
plt.legend(loc='lower right');
plt.xlabel("distance")
plt.ylabel("velocity")
plt.show()


# In[144]:


from sklearn.metrics import accuracy_score 


# In[145]:



accuracy = accuracy_score(y, log_reg_pred)
# Coefficient of the features in the decision function. (from theta 1 to theta n)
parameters = log_reg.coef_[0]
# Intercept (a.k.a. bias) added to the decision function. (theta 0)
parameter0 = log_reg.intercept_


# In[146]:


# Plotting the decision boundary
fig = plt.figure(figsize=(10,7))
x_values = [np.min(X[:, 1] -5 ), np.max(X[:, 1] +5 )]
# calcul y values
#y_values = - (parameter0 + np.dot(parameters[0], x_values)) / parameters[1]
y_values = np.dot((-1./parameters[1]), (np.dot(parameters[0],x_values) + parameter0))
colors=['red' if l==0 else 'blue' for l in y]
plt.scatter(X[:, 0], X[:, 1], label='Logistics regression', color=colors)
plt.plot(x_values, y_values, label='Decision Boundary')
plt.xlabel('Marks in 1st Exam')
plt.ylabel('Marks in 2nd Exam')
plt.show()

