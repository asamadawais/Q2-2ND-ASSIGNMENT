#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[3]:


import numpy as np
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(2, 5)
x


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[6]:


x = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
y = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
z = np.vstack((x, y))
z


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[7]:


x = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
y = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
z = np.hstack((x, y))
z


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[8]:


x = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
y = np.ravel(x)
y


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[23]:


a = np.array([[0, 1, 2, 3, 4] , [5, 6, 7, 8, 9], [ 10, 11, 12, 13, 14]])
b = np.ravel(a)
b


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[37]:


x = np.arange(15).reshape(5, 3)
x


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[5]:


a = np.arange(25).reshape(5, 5)
x = np.square(a)
x


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[12]:


a = np.arange(30).reshape(5, 6)
print(a)
x = np.mean(a)
x


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[11]:


a = np.arange(30).reshape(5, 6)
print(a)
x = np.std(a)
x


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[13]:


a = np.arange(30).reshape(5, 6)
print(a)
x = np.median(a)
x


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[16]:


a = np.arange(30).reshape(5, 6)
print(a)
x = np.transpose(a)
x


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[17]:


import numpy as np
a = np.arange(16).reshape(4, 4)
print(a)
x = np.trace(a)
x


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[22]:


a = np.arange(16).reshape(4, 4)
print(a)
x = np.linalg.det(a)
x


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[25]:


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("arr : ", arr) 
print("5th percentile of arr : ", 
       np.percentile(arr, 5))
print("95th percentile of arr : ",
       np.percentile(arr, 95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[36]:


#EXample 1
a = np.arange(16).reshape(4, 4)
print(a)
x = np.isnan(a)
print(x)


# In[41]:


b = np.arange(25).reshape(5, 5)              
print("\nIs NaN: \n", np.isnan(b))     
c = [[1,2,3],  
     [np.nan,2,2]] 
print("\nIs NaN: \n", np.isnan(c))


# In[ ]:




