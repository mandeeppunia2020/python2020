#!/usr/bin/env python
# coding: utf-8

# In[1]:


students=['mandeep','anu','muskan','suman','rohit']

print(students[2])


# In[2]:


print(students[0].title())


# In[6]:


print(students)


# In[ ]:





# In[ ]:


Req:

How to add the new element to the list..?    
How to edit the element from the list..?
How to delete the element from the list..?


# In[ ]:


How to add the new element to the list..?

Req: i want to add the "sandeep " to the above list...?


# In[8]:


students.append('sandeep')


# In[9]:


print(students)


# In[ ]:


Req: i want to add "kaafi" to the above list..?


# In[13]:


students.append('kaafi')# append will be adding the element to the last  of the list.. 

print(students)


# In[ ]:


Req: i want to add 'harman' to the above list at 3rd place..?


# In[14]:


students.insert(2,'harman')

print(students)


# In[ ]:


2. hoe to edit the element from a list..?


# In[ ]:


Req: i want to replace anu with smile..


# In[15]:


students[1]='smile'

print(students)


# In[ ]:


3. How to delete the element from the list...?


# In[ ]:


Req: i want to delete suman from the list..


# In[16]:


del students[4]

print(students)


# In[ ]:




