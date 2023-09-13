#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#FunctionDefinition


# In[1]:


big = max('Hello world')
print(big)


# In[3]:


tiny = min('Hello world')
print(tiny)


# In[ ]:


#Type Conversions


# In[4]:


print(float(99) / 100)


# In[ ]:


#Building our Own Functions


# In[18]:


x = 5
print('Hello')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
x = x + 2
print(x)


# In[ ]:


#Definitions and Uses


# In[19]:


x = 5
print('Hello')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
print_lyrics()
x = x + 2
print(x)


# In[ ]:


#Multiple Parameters / Arguments


# In[20]:


def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)


# In[ ]:


#Exercise


# In[ ]:




