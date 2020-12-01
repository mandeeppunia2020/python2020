#!/usr/bin/env python
# coding: utf-8

# In[ ]:


String :
    ----->string motheds.
    type
    title
    upper
    lower
    
    f string


# In[ ]:


Adding whitespace to strings:


# In[1]:


print("names:mandeepmuskansumananurohit")


# In[ ]:


adding new line delimeter:\n


# In[3]:


print("names:\nmandeep\nmuskan\nravi\nanu\nrohit")


# In[6]:


print("names:\n\tmandeep\n\tmuskan\n\travi\n\tanu\n\trohit")#new line with space delimeter:


# In[ ]:





# In[ ]:


Removing whitespace from the string:


# In[7]:


x='mandeep'

print(x)


# In[8]:


y='   mandeep'

print(y)


# In[9]:


z='mandeep   '
print(z)


# In[ ]:


Stripping commands to remove whitespace form the string:


# In[10]:


y.lstrip()# left side stripping


# In[11]:


z.rstrip()# right side stripping


# In[13]:


A="     mandeep punia     "

print(A.title())


# In[14]:


A.strip()# left and right side gaps will be elimanted..!--> in two steps: 1.Search 2.Elimated


# In[ ]:





# In[ ]:


Introduction to list datatype:


# In[ ]:


Defination: A list ia an ordered collection of items.

Classification: A list is classified as an mutable(which can be editable)datatype.

How to define the list...? [] #square brackets.


# In[ ]:





# In[17]:


student=['mandeep','muskan','anu','rohit','ravi','sai']

print(student)


# In[18]:


type(student)


# In[ ]:


Req: how to acess the element form the list..?


# In[ ]:


introdcion to indexing: 0,1,2,3......


# In[ ]:





# In[ ]:


Req: i wnat to acess muskan from above list...?


# In[19]:


print(student[1])


# In[20]:


print(student[3].upper())


# In[22]:


print(student[3].title())


# In[ ]:





# In[ ]:




