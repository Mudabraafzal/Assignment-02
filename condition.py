#!/usr/bin/env python
# coding: utf-8

# In[10]:


x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')    
print('Finis')


# In[ ]:


#Comparison Operators 


# In[13]:


x = 5
if x == 5 : 
    print('Equals 5')
if x > 4 : 
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equals 5')
if x < 6 : print('Less than 6') 
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :  
    print('Not equal 6')


# In[ ]:


#Nested Decisions


# In[15]:


x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('Less than 100')    


# In[ ]:


#Two-way Decisions with else


# In[18]:


x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')    


# In[ ]:


#Multi-way


# In[19]:


if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('LARGE')    


# In[22]:


x = 5
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
print('All done') 


# In[ ]:


#Multi-way Puzzles


# In[23]:


if x < 2 :
    print('Below 2')
elif x >= 2 : 
    print('Two or more')
else :
    print('Something else')


# In[ ]:


#print('Second', istr)


# In[25]:


astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)    

