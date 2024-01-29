#!/usr/bin/env python
# coding: utf-8

# ### Homogenous List

# In[43]:


list1=[1,2,3,4,5,6,7,8,9,10]             # create list (creates obj of list class)
print(list1)

print(type(list1))                       # Type of var list1

print(list1[8]==list1[-2])               # +ve and -ve indexing

print(list1[2:6])                        # Slicing

print(len(list1))                        # Length Function

print(list1[15])                         #Indexing (Throws error due to index out of range)

o/p-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
<class 'list'>
True
[3, 4, 5, 6]
10
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[43], line 12
      8 print(list1[2:6])
     10 print(len(list1))
---> 12 print(list1[15])

IndexError: list index out of range

# ### Heterogenous List

# In[14]:


list2=[1,5,9.5,'VB',[3,6.5,'AB']]       

print(list2)
print(list2[-1])
print(list2[-1][2])
print(len(list2))
print(list2[0:10])

o/p-> [1, 5, 9.5, 'VB', [3, 6.5, 'AB']]
[3, 6.5, 'AB']
AB
5
[1, 5, 9.5, 'VB', [3, 6.5, 'AB']]

# In[20]:


print(list2[:])
print(list2[::-1])
print(list2[0:4:-1])
print(list1[:5])
print(list1[5:])

o/p-> [1, 5, 9.5, 'VB', [3, 6.5, 'AB']]
[[3, 6.5, 'AB'], 'VB', 9.5, 5, 1]
[]
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]

# In[21]:


list2[:]
list2[::-1]

o/p-> [[3, 6.5, 'AB'], 'VB', 9.5, 5, 1]

# ## Functions

# In[27]:


list1.append(25)   # adds elements at the end of list
list1

o/p-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25]

# In[28]:


list1.insert(3,50) # Inserts element at particular index
list1

o/p-> [1, 2, 3, 50, 4, 5, 6, 7, 8, 9, 10, 25]

# In[31]:


list1.extend(['1','3','5'])            #adds multiple elements/list at the end
list1

o/p-> [1, 2, 3, 50, 4, 5, 6, 7, 8, 9, 10, 25, '1', '3', '5']

# In[34]:

new=[]
for i in range(1,len(list1)+1):        # Reverses List
    new.append(list1[-i])
print(new)

o/p-> ['5', '3', '1', 25, 10, 9, 8, 7, 6, 5, 4, 50, 3, 2, 1]

# In[35]:


list1.pop(3)            #removes 3rd index element
list1

o/p-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, '1', '3', '5']

# In[36]:


list1.pop()             # removes last element
list1

o/p-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, '1', '3']

# In[37]:


list1.remove(9)         # removes the element from list
list1

o/p-> [1, 2, 3, 4, 5, 6, 7, 8, 10, 25, '1', '3']

# In[38]:


del list1[3]            # deletes the indexed element from list
list1

o/p-> [1, 2, 3, 5, 6, 7, 8, 10, 25, '1', '3']

# In[39]:

del list1[1:4]
list1

o/p-> [1, 6, 7, 8, 10, 25, '1', '3']

# In[40]:

del list1    # removes list1 from memory location


# In[41]:


list1

NameError                                 Traceback (most recent call last)
Cell In[25], line 1
----> 1 list1

NameError: name 'list1' is not defined

# In[49]:

list1=[1, 6, 7, 8, 10, 25, '1', '3']
list1.clear()          #Empties the list, but variable remains in memory location
list1

o/p-> []
# In[52]:


# WAP to separate even and odd elements

lst=[1,2,3,4,5,6,7,8,9,10]

even=[]
odd=[]

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

o/p-> even: [2, 4, 6, 8, 10]
      odd: [1, 3, 5, 7, 9]
# In[53]:


even=lst[1::2]
odd=lst[0::2]
print(even)
print(odd)

o/p-> even: [2, 4, 6, 8, 10]
      odd: [1, 3, 5, 7, 9]

# In[2]:


list1=[1,3,5,3.6,'A','B','53']


# In[3]:

# WAP to swap 2 elements

el_1=eval(input('Enter 1st element to swap '))
el_2=eval(input('Enter 2nd element to swap '))
tmp,tp,j,m=0,0,0,0
for i in range(len(list1)):
    if list1[i]==el_1:
        tmp=list1[i]
        j=i
        print(tmp)
    if list1[i]==el_2:
        tp=list1[i]
        m=i
        print(tp)
list1[j]=tp
list1[m]=tmp

Enter 1st element to swap 3
Enter 2nd element to swap 3.6
3
3.6

# In[4]:

list1

o/p-> [1, 3.6, 5, 3, 'A', 'B', '53']

# In[6]:

list1=[23,76,8,12,83,69,53,90,24,35,68,37]

minn=list1[0]
maxx=0

for i in range(len(list1)):
    if list1[i]>maxx:
        maxx=list1[i]
        
    if list1[i]<minn:
        minn=list1[i]
print('Maximum Element ',maxx)
print('Minimum Element ',minn)

o/p-> Maximum Element  90
      Minimum Element  8

# In[ ]:




