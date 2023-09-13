#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#exercise


# In[3]:


hours =input ("enter Hours")
h=int(hours)
rate =input ("enter rate")
r=int (rate)
if h <= 40:
    print(h*r)
elif h>40:
    print(40*r+(h-40)*1.5*r)


# In[4]:


hours=input("Enter Hours:")
try:
  int(hours)
  rate=input("Enter Rate:")
  int(rate)
  pay = int(hours) * int(rate) 
  int(pay)
  print("Pay:")
  print(pay)
except: 
  print("Error, please enter a number.  Please run the program again.")


# In[ ]:




