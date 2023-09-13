#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Inside Strings


# In[1]:


fruit = 'banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)


# In[ ]:


#Have Length


# In[2]:


fruit = 'banana'
print(len(fruit))


# In[ ]:


#len Function


# In[3]:


fruit = 'banana'
x = len(fruit)
print(x)


# In[ ]:


#Looping Through Strings


# In[4]:


fruit = 'banana'
index = 0
while index < len(fruit): 
    letter = fruit[index]
    print(index, letter)
    index = index + 1


# In[5]:


fruit = 'banana'
for letter in fruit: 
    print(letter)


# In[6]:


fruit = 'banana'
for letter in fruit : 
    print(letter)
    index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(letter)
    index = index + 1


# In[ ]:


#Looping and Counting


# In[7]:


word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)


# In[ ]:


#String Operations


# In[8]:


s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
      
      
      


# In[ ]:


#Slicing Strings


# In[9]:


s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])


# In[ ]:


#String Concatenation


# In[10]:


a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)


# In[ ]:


#String Comparison


# In[11]:


if word == 'banana':
    print('All right, bananas.')
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')


# In[ ]:


#String Library


# In[14]:


greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())


# In[ ]:


#Parsing and Extracting


# In[ ]:


From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008


# In[15]:


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)


# In[ ]:


#Prefixes


# In[20]:


line ='Please have a nice day'
line.startswith('Please')


# In[21]:


line.startswith('p')


# In[ ]:


#Stripping Whitespace


# In[22]:


greet = ' Hello Bob '
greet.lstrip()
greet.rstrip()
' Hello Bob'
greet.strip()
'Hello Bob'


# In[ ]:


#UPPER CASE


# In[23]:


greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)


# In[ ]:


#Search and Replace


# In[25]:


greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
nstr = greet.replace('o','X')
print(nstr)


# In[ ]:


#Searching a String


# In[26]:


fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)


# In[ ]:




