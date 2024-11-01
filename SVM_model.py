#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from joblib import dump,load
import matplotlib.pyplot as plt


# #import necessay librabries
# 

# In[2]:


#importing dataset and splitting it into X and y [X:contains 5 features,y:contains the output i.e '1' or '0']
df=pd.read_csv('Data.csv')
df.head()
X=df.iloc[:,[0, 1, 2, 3, 4]].values
y=df.iloc[:, 5].values


# In[3]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)


# In[4]:


#Features scaling the dataset
sc=StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[5]:


# Fitting SVM to the Training set

clf= SVC(kernel = 'linear', random_state = 0)
clf.fit(X_train, y_train)



# In[6]:


#predicting the data
y_predict=clf.predict(X_test)
dataset=pd.read_csv('Live.csv')
dataset
result=clf.predict(dataset)
print(result)



# In[7]:


# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_predict)
#cu=classification_report(y_test,y_predict)

#print(cu)


# In[8]:


#save the model for further use
dump(clf,"final_SVM_model.sav")


# In[ ]:





# In[ ]:





# In[ ]:




