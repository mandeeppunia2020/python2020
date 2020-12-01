#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to looping statments:


# In[6]:


student=['sandeep','pardeep','vikash','muskan','renu']

print(student)


# In[4]:


type(student)


# In[ ]:


Req: i want to apreciate each and every student in the above list for submitting their work daily.


# In[9]:


print(f"keep up the good work,{student[0].title()}")


# In[11]:


print(f"keep up the good work,{student[3].title()}")


# In[ ]:


# gernal syntax of a for loop:


# In[ ]:


for tempvariable in mainvariable:
    print(tempvariable)# this gap is called indentation...


# In[14]:


for x in student:
    print(f"keep up good work,{x.title()}")


# In[18]:


for x in student: # this whole process is called as iteration the elements..
    print(x)


# In[19]:


for x in student:
    print(f"keep up good work,{x.title()}")
    print(f"i am looking forword to receive all your practice file,{x.title()}")


# In[20]:


for x in student:
    print(f"keep up good work,{x.title()}")
    print(f"i am looking forword to receive all your practice file,{x.title()}\n")


# In[ ]:


# in the loop and out of the loop:


# In[ ]:


Req: i want to convey thanks to all for joining in the classes...


# In[23]:


for x in student:
    print(f"keep up good work,{x.title()}")
    print(f"i am looking forword to receive all your practice file,{x.title()}\n")
print("Thanks all of you for joining in the session on time ..")    


# In[ ]:





# In[ ]:


organining the list:


# In[ ]:


student=['sandeep','pardeep','vikash','muskan','renu']


# In[ ]:


Req: i want to know the total count of the students..


# In[24]:


len(student)# i will give the total count of the element in the list...


# In[ ]:





# In[ ]:





# In[ ]:




