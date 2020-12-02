#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Organising the list datatype:


# In[ ]:





# In[1]:


car=['maruthi','bmw','honda','benz','tayota']

print(car)


# In[ ]:


Req: i want to know total count of the car....!


# In[2]:


len(car)


# In[ ]:


Req: i want to organize the list in the alphabetical order----->A-Z


# In[ ]:


two diffrent approcahes:
    1. temp approach
    2. per approach


# In[ ]:


Note. in the temp approach we will be having the original order of the list.


# In[ ]:





# In[3]:


print(sorted(car)) #benz, bmw....e,m


# In[ ]:





# In[ ]:


permanent approach:


# In[5]:


car.sort()


# In[9]:


print(car)


# In[10]:


print(car)# the change are implied permanently....!


# In[ ]:


get_ipython().set_next_input('interview:1. what is the diffrence btw sorted and sort methods in a list');get_ipython().run_line_magic('pinfo', 'list')
          2. how do you count the total element in a list ? by using which method...?


# In[ ]:





# In[ ]:


Req: how do you print a list in a reverse order....?


# In[11]:


car.reverse()


# In[12]:


print(car)


# In[13]:


print( car)# the changes are the permanently....!


# In[ ]:





# In[ ]:


slicing the list


# In[14]:


mystudent=['mandeep','punia','muskan','poona','vikram','sshil','vishal','renu']

print(mystudent)


# In[ ]:


Gernal syntax of a slicing...>totally dependent on indexing:
    var[startvalue:stopvalue:stepcounter]


# In[ ]:


Req: i want to make a team of two student each:
 
Note: last value is always exclusive **


# In[15]:


print(mystudent[0:1])


# In[16]:


print(mystudent[0:2])# we have to increment the index by 1 to include the pervious element...!


# In[17]:


print(mystudent[2:4])


# In[18]:


print(mystudent[4:6])


# In[21]:


print(mystudent[6:8])


# In[ ]:





# In[22]:


print(mystudent)


# In[ ]:


Req: i want pair of one after another of student:


# In[23]:


print(mystudent[0:8:2])


# In[ ]:





# In[ ]:


introduction tp negative indexing: -1,-2,-3....>


# In[24]:


print(mystudent)


# In[ ]:


Req: to access renu by  using -ve indexing..?


# In[25]:


print(mystudent[-1])


# In[26]:


print(mystudent[7])# +ve indexing


# In[ ]:




