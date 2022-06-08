#!/usr/bin/env python
# coding: utf-8

# # Python program to interchange first and last elements in a list
# Given a list, write a Python program to swap first and last element of the list.
# Examples: 
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
# 
# Input : [1, 2, 3]
# Output : [3, 2, 1]

# In[3]:


l1=[1,2,3,4,5]
l1[0],l1[-1]=l1[-1],l1[0]
l1


# In[18]:


a=[12,35,9,56,24]

length = len(a)
length = len(b)

temp = a[0]
a[0] = a[length - 1]
a[length - 1] = temp

print(a)


# In[ ]:


I = [12, 35, 9, 56, 24]
p=I[-1]
s=I.pop(0)
q=I.pop()
I.append(s)
I.insert(0,p)
print(I)


# # WAP to find length of list
# The list is : [1, 4, 5, 7, 8]
# Length of list is : 5
# 

# In[9]:


l1=[1, 4, 5, 7, 8]
print("Length of list is : ",len(l1))


# In[15]:


l1=[1, 4, 5, 7, 8, 9]
print("Length of list is : ",l1.index()+1)


# In[11]:


l1=[1, 4, 5, 7, 8]
count=0
for i in l1:
    count+=1
print("Length of list is : ",count)


# # WAP to Check if element exists in list 
# 
# Checking if 4 exists in list : 
# Element Exists
# 

# In[19]:


l1=[1, 4, 5, 7, 8]
n=4
if 4 in l1:print("Element Exists")


# In[26]:


l1=[1, 4, 5, 7, 8]
for i in range(len(l1)):
    if l1[i]==4:print("Element Exists")


# # WAP to clear a list
# before clear: [6, 0, 4, 1]
# 

# In[33]:


l1=[1, 4, 5, 7, 8]
l1.clear()
l1


# In[38]:


l1=[1, 4, 5, 7, 8]
for i in range (len(l1)):
    l1.remove(l1[-1])
l1


# In[81]:


l1=[1, 4, 5, 7, 8]
for i in range (len(l1)):
    l1.pop()
l1


# In[84]:


l1=[1, 4, 5, 7, 8]
l1=[]
l1


# In[85]:


l1=[1, 4, 5, 7, 8]
l1*=0
l1


# # WAP to Reversing a List
# Input : list = [10, 11, 12, 13, 14, 15]
# Output : [15, 14, 13, 12, 11, 10]
#  
# Input : list = [4, 5, 6, 7, 8, 9]
# Output : [9, 8, 7, 6, 5, 4]
# 

# In[44]:


l1 = [10, 11, 12, 13, 14, 15]
l1.reverse()
l1


# In[45]:


l1 = [10, 11, 12, 13, 14, 15]
for i in range(len(l1)):
    a=l1.pop()
    l1.insert(i,a)
l1


# In[46]:


a=[10, 11, 12, 13, 14, 15]
if len(a)%2!=0:
    c=1
    for i in range(round(len(a)/2)-1):
            a[i]=a[i]+a[len(a)-c]
            a[len(a)-c]=a[i]-a[len(a)-c]
            a[i]=a[i]-a[len(a)-c]
            c+=1
else:
    c=1
    for i in range(round(len(a)/2)):
            a[i]=a[i]+a[len(a)-c]
            a[len(a)-c]=a[i]-a[len(a)-c]
            a[i]=a[i]-a[len(a)-c]
            c+=1
print(a)


# # Given a list of numbers, write a Python program to find the sum of all the elements in the list.
# Example: 
#  
# Input: [12, 15, 3, 10]
# Output: 40
#  
# Input: [17, 5, 3, 5]
# Output: 30
# 

# In[47]:


l1=[12, 15, 3, 10]
print(sum(l1))


# In[48]:


l1=[12, 15, 3, 10]
sum1=0
for i in l1:
    sum1+=i
print(sum1)


# # Given a list of numbers, the task is to write a Python program to find the second largest number in the given list.
# Examples: 
# Input: list1 = [10, 20, 4]
# Output: 10
# Input: list2 = [70, 11, 20, 4, 100]
# Output: 70
# 

# In[69]:


list1 = [70, 11, 20, 4, 100] 
list1.sort()
list1[-2]


# In[50]:


list1 = [70, 11, 20, 4, 100] 
list2=list1
list2.remove(max(list2))
print(max(list2))


# In[72]:


list1 = [70, 11, 20, 4, 100, 100] 
list2=list(set(list1))
list2.sort()
list2.pop()
list2[-1]


# # Given a list of integers, the task is to find N largest elements assuming size of list is greater than or equal o N.
# Examples :
# Input : [4, 5, 1, 2, 9] 
#         N = 2
# Output :  [9, 5]
#  
# Input : [81, 52, 45, 10, 3, 2, 96] 
#         N = 3
# Output : [81, 96, 52]
# 

# In[80]:


l1=[81, 52, 45, 10, 3, 2, 96] 
n=int(input())    #4
l2=list(set(l1))
l2.sort()
l2[-(n):]


# In[87]:


l1=[81, 52, 45, 10, 3, 2, 96] 
n=int(input())
l2=list(set(l1))
l2.sort()
l3=[]
for i in range(n):
    a=l2.pop()
    l3.append(a)
l3
    


# In[89]:


l1=[81, 52, 45, 10, 3, 2, 96] 
n=int(input())
l2=list(set(l1))
l2.sort()
l3=[]
for i in range(len(l2)-n,len(l2)):
    l3.append(l2[i])
l3
    


# In[90]:


n=int(input())
l1=[81, 52, 45, 10, 3, 2, 96] 
l1=sorted(l1,reverse=True)

l2=[]
for i in range(n):
    l2.append(l1[i])
print(l2)


# # Given a list of numbers, write a Python program to remove multiple elements from a list based on the given condition.
# Example: 
# Input: [12, 15, 3, 10]
# Output: Remove = [12, 3], New_List = [15, 10]
#  
# Input: [11, 5, 17, 18, 23, 50]
# Output: Remove = [1:5], New_list = [11, 50]
# 

# In[4]:


l1= [12, 15, 3, 10] 
Remove=[12,3]
for r in Remove:
    l1.remove(r)
print("New_list=",l1)


# In[5]:


l1= [12, 15, 3, 10] 
Remove=[12,3]
for r in Remove:
    i=l1.index(r)
    l1.pop(i)
print("New_list=",l1)


# In[26]:


l1= [11, 5, 17, 18, 23, 50]
ip=input("Remove = ")
ip=ip.strip('[]')
Remove=list(map(str,ip))
if Remove[1]==":":
    j1=int(Remove[0])
    j2=int(Remove[2])
    redu=0
    for k in range(j1,j2):
        l1.pop(k-redu)
        redu+=1
print("New_list=",l1)


# Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
#          x = 10
# Output : 3 
# 10 appears three times in given list.
#  
# Input : lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
#         x = 16
# Output : 0
# 

# In[28]:


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x=int(input("Enter the number"))
lst.count(x)


# In[36]:


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x=int(input("Enter the number"))
count=0
for y in lst:
    if y==x:
        count+=1
count


# In[ ]:





# # Given a list of integers with duplicate elements in it. The task to generate another list, which contains only the duplicate elements. In simple words, the new list should contain the elements which appear more than one.
# Examples : 
# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]
#  
#  
# Input :  list = [-1, 1, -1, 8]
# Output : output_list = [-1]
# 

# In[46]:


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
list2 = [-1, 1, -1, 8]
#val=set(list1)
val=set(list2)
op=[]
for i in val:
    #j=list1.count(i)
    j=list2.count(i)
    if j>1:
        op.append(i)
print(op)


# In[ ]:





# # Python program to find Cumulative sum of a list
# The problem statement asks to produce a new list whose i^{th} element will be equal to the sum of the (i + 1) elements.
# Examples : 
#  
# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]
#  
# Input : list = [4, 10, 15, 18, 20]
# Output : [4, 14, 29, 47, 67]
# 

# In[41]:





# # Break a list into chunks of size N in Python
# Input: [1, 2, 3, 4, 5,6, 7, 8, 9]
# Output: [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
# 

# In[ ]:





# # Remove common elements from two list in Python

# In[47]:


l1=[2,4,5,6,8,10,12,14,16,18]
l2=[3,6,9,12,15,18]
for i in l1:
    if (i in l1) and (i in l2):
        l1.remove(i)
        l2.remove(i)
print(l1)
print(l2)


# In[48]:





# Given a list of numbers, write a Python program to remove multiple elements from a list based on the given condition. Example: Input: [12, 15, 3, 10] Output: Remove = [12, 3], New_List = [15, 10]
# 

# In[ ]:


a=[12,15,3,10]
b=[12,3,2]
for i in b:
    if i in a:
        a.remove(i)
print(a)


# In[ ]:


a=[12,15,3,10]
b=[12,3,2,10]
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j]:
            a.pop(j)
print(a)


# In[ ]:


a=[12,15,3,10]
b=[12,3,2]
for i in b:
    if i in a:
        a.pop(a.index(i))
print(a)


# In[ ]:


a=[12,15,3,10]
b=[12,3,2]
a = [ele for ele in a if ele not in b]
print(a)


# In[ ]:


a= [11, 5, 17, 18, 23, 50]
b= a[1:5]
for i in b:
    if i in a:
        a.pop(a.index(i))
print(a)


# Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10] x = 10 Output : 3 10 appears three times in given list.
# 
# Input : lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] x = 16 Output : 0

# In[1]:


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10] 
lst.count(10)


# In[ ]:


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10] 
x=10
c=0
for i in lst:
    if x==i:
        c+=1
print(c)


# Given a list of integers with duplicate elements in it. The task to generate another list, which contains only the duplicate elements. In simple words, the new list should contain the elements which appear more than one. Examples : Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20] Output : output_list = [20, 30, -20, 60]

# In[ ]:


list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
#s=set(list)
b=[]
c=[]
for i in list:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print(set(c))


# In[ ]:


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
list2=[]
for i in list1:
    a=list1.count(i)
    if a!=1:
        for j in range(a-1):
            list1.remove(i)
        list2.append(i)
print(list2)


# In[ ]:


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
set1=set(list1)
list2=[]
for i in set1:
    c=0
    for j in list1:
        if i==j:
            c+=1
    if c>1:
        list2.append(i)

print(list2)


# Python program to find Cumulative sum of a list The problem statement asks to produce a new list whose i^{th} element will be equal to the sum of the (i + 1) elements. Examples :
# 
# Input : list = [10, 20, 30, 40, 50] Output : [10, 30, 60, 100, 150]
# 
# Input : list = [4, 10, 15, 18, 20] Output : [4, 14, 29, 47, 67]

# In[ ]:


l1 = [10, 20, 30, 40, 50]
l2=[]
a=0
for i in range(len(l1)):
    a+=l1[i]
    l2.append(a)
print(l2)


# In[ ]:


list1 = [10, 20, 30, 40, 50]

list2=[]
for i in range(0,len(list1)):
    if i!=0:
        a=list2[i-1]+list1[i]
        list2.append(a)
    else:
        list2.append(list1[i])

print(list2)


# In[ ]:


list1 = [10, 20, 30, 40, 50]
l2=[]
l2.append(list1[0])
for i in range(len(list1)-1):
        
        a=l2[i]+list1[i+1]
        l2.append(a)
print(l2)


# Break a list into chunks of size N in Python Input: [1, 2, 3, 4, 5,6, 7, 8, 9] Output: [[1, 2, 3, 4], [5, 6, 7, 8], [9]]

# In[ ]:


l1=[1, 2, 3, 4, 5,6, 7, 8, 9,10,11]
n=4
l2=[]
for i in range(0,len(l1),4):
    l4=l1[i:i+n]
    l2.append(l4)
    
print(l2)


# In[ ]:


list = [10, 20, 30, 40,50] 
l=sorted(list)
list2 = [4, 10, 15, 18, 20]
for i in l:
    if i in list2:
        list.remove(i)
        list2.remove(i)
print(list)
print(list2)


# In[ ]:




