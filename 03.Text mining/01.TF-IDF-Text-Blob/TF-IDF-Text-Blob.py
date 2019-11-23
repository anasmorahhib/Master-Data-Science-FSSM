#!/usr/bin/env python
# coding: utf-8

# """
# Created on Wed Sep 25 16:03:49 2019
# @author: Master DS By Anas Morahhib
# """

# In[1]:


from textblob import TextBlob 
import numpy as np
import math
import re
import pandas as pd


# In[18]:


documents = [
        "You are trying to code TF-IDF all by youreself like a big boy.",
        "So this is a tinny doc.",
        "And another tinny doc to test few stuff.",
        "So in total, we are four documents, have fun ;)."
]


# In[19]:


def clean_doc (d):
    d = d.lower()
    return re.sub('[^a-z0-9\-]+', ' ', d)


# #  Question 1

# tf(t,d) = count of t in d / number of words in d

# In[20]:


def tf(w,d):
    d = clean_doc (d)
    d1 = d.split()
    d1 = tuple(d1)
    return d1.count(w) / len(d1)


# # Question 2

# In[21]:


def idf(w,D):
        df = 0
        N = len(D)
        for i in range (0, N):
            c =  D[i].count(w)
            df += 1 if c > 0 else 0
        return math.log(N/(df+1))


# # Question 3

# In[22]:


def tf_idf(w,d,D):
    # Caluculer TF
    # tf(t,d) = count of t in d / number of words in d
    d1 = TextBlob(d)
    count_td = d1.word_counts[w]
    number_w = len(d1.words)
    tf = count_td / number_w 
    # calculer idf
    # idf(t) = log(N/(df + 1))
    df = 0
    N = len(D)
    
    # df(t) = occurrence of t in documents
    for i in range (0, N):
        d = TextBlob(D[i])
        c = d.word_counts[w]
        df += 1 if c > 0 else 0
    idf = math.log(N/(df+1))
    
    # tf-idf(t, d) = tf(t, d) * log(N/(df + 1))
    
    return tf*idf


# # Question 4

# In[23]:


val1 = tf("boy", documents[0])
print('TF for word "boy" = ',val1)
val2 = idf("boy", documents)
print('IDF for word "boy" = ',val2)
print('TF-IDF without TextBlob', val1*val2 )
val = tf_idf("boy", documents[0], documents)
print('TF-IDF with TextBlob" = ',val)


# # Question 5
# 

# In[24]:


def docs_to_words (D):
    words = []
    for i in range (0, len(D)):
        d = TextBlob(D[i].lower())
        words = set(words).union(set(d.words))
    return words    


# ### Création et affichage du TDM et DTM

# In[86]:


# Count TF-IDF for evry words in evry documents 
wordSet = docs_to_words(documents)
wordsDocsCount = []
for i in range(0, len(documents)):
    wordsCount = {}
    for word in wordSet:
         wordsCount[word] = tf_idf(word,documents[i],documents)
    wordsDocsCount.append(wordsCount)

# Creation et affichage du TDM
print(np.transpose(pd.DataFrame(wordsDocsCount)))

#Creation et affichage du DTM 
print(pd.DataFrame(wordsDocsCount))


# # Question 6
# 

# In[95]:


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
#Creation et affichage du DTM 
X = vectorizer.fit_transform(documents)
print(X)


# # Question 7
# 

# #### Les deux matrices du question 5 et 6 ne sont pas identique:
# #### La visualisation:
# Dans la question 5 on affiche les documents en colonnes et les features en lignes et la valeur tf-idf et l'intersection entre les deux.
# Par contre dans la question 6 on a deux colonnes, la premier colonne est pour identifier un mot par l'indice de son document et son indice dans la liste des mots et la deusième c'est sa valeur tf-idf.
# Ce type de matrice s'appelle une matrice creuse, selon wikipedia c'est une matrice contenant beaucoup de zéros, Ces données sont facilement compressibles, et cette compression amène presque à chaque fois une baisse significative de la consommation mémoire.
# 

# # Question 8
# 

# In[98]:


import os
import nltk
import nltk.corpus


# #### import data

# In[99]:


docs = []
d1 = nltk.corpus.gutenberg.raw('shakespeare-caesar.txt')
d2 = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')
d3 = nltk.corpus.gutenberg.raw('shakespeare-macbeth.txt')

docs.append(d1)
docs.append(d2)
docs.append(d3)


# #### Creation et affichage du DTM 
# 

# In[100]:


vectorizer = TfidfVectorizer(ngram_range=(1, 2))
#Creation et affichage du DTM 
X = vectorizer.fit_transform(docs)


# In[101]:


print(X.shape)
print(X)
      


# In[ ]:




