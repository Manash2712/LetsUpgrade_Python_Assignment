
# coding: utf-8

# # Day 2
# 

# In[1]:


#List and its Functions

lst = []
lst.append(1) #adds element to the last
print(lst)


# In[2]:


lst.insert(1,2)  #inserrt at particular position
print(lst)


# In[3]:


lst2 = [3,4]
lst.extend(lst2)  #joins 2 lists
print(lst)


# In[4]:


print(sum(lst))  


# In[5]:


print(lst.count(1))  #return count of particular element


# In[6]:


print(len(lst))  #returns length of list


# # Dictionaries

# In[7]:


#Creating and Printing
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)


# In[9]:


#Accessing item
x = thisdict["model"]
print(x)


# In[10]:


x = thisdict.get("model")
print(x)


# In[11]:


thisdict["year"] = 2018 #CHANGING THE VALUE
print(thisdict)


# In[12]:


thisdict.pop("model")  #rwmoving an element
print(thisdict)


# In[13]:


thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
del thisdict["model"]  #removes item with specified keyname
print(thisdict)


# In[14]:


thisdict.clear()  #empties the dictionary
print(thisdict)


# # Sets

# In[15]:


my_set = {1, 2, 3}
print(my_set)


# In[17]:


my_set.add(4)  #adds particular element
print(my_set)


# In[18]:


my_set.update([5, 6, 7])  #adds multiple elements
print(my_set)


# In[19]:


my_set.discard(4)  #removing element
print(my_set)


# In[20]:


my_set.remove(6)
print(my_set)


# In[21]:


print(my_set.pop()) #removes random element


# In[22]:


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A.union(B)


# In[23]:


B.union(A)


# In[24]:


A.intersection(B)


# In[25]:


A.difference(B)


# In[26]:


B.difference(A)


# In[27]:


A.symmetric_difference(B)


# # Tuples

# In[28]:


my_tuple = ()  #creating empty tuple
print(my_tuple)


# In[29]:


my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p')) 
print(my_tuple.index('l')) 


# In[30]:


print('a' in my_tuple)
print('b' in my_tuple)

