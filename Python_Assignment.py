#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to sum all the items in a list.  
#  

# In[15]:


def sum_list(items):
    sum_no=0
    for i in items:
        sum_no+=i
    return sum_no


# In[16]:


print(sum_list([1,2,3,4]))


# ### 2. Write a Python program to multiplies all the items in a list.

# In[17]:


def mul_list(list):
    mul_no=1
    for i in list:
        mul_no*=i
    return mul_no 


# In[18]:


print(mul_list([1,2,3,4]))


# ### 3.Write a Python program to get the largest number from a list.  

# In[31]:


def large_no( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max  


# In[30]:


print(large_no([1, 2,3,4]))  


# ### 4. Write a Python program to get the smallest number from a list.  

# In[32]:


def small_no(list):
    min = list[0]
    for a in list:
        if a < min:
            min =a
    return min


# ### 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

# In[1]:


def abc(list):
    counter=0
    for i in list:
        if len(i)>2 and i[0]==i[-1]:
            counter+=1
    return counter


# In[6]:


print(abc(['abc','sarvesh','aa','nayan','35363']))


# ### 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

# In[ ]:





# ### 7. Write a Python program to remove duplicates from a list.  

# In[3]:


def dup(list):
    a=set(list)
    return a


# In[4]:


print(dup([1,4,6,8,9,5,9,2,6,9]))


# In[16]:


a=[10,20,30,40,40,50,10,30,50,90,10]
c=set(a)
print(c)
b=[]
for i in c:
    b.append(i)
print(sorted(b))


# ### 8. Write a Python program to check a list is empty or not.  
# 

# In[11]:


b=[]
while True:
    c=input("enter list element: ")
    if c=="":
        break
    b.append(int(c))
print(b)
if i not in b:
    print("list is empty")
else:
    print("Not Empty")


# ### 9. Write a Python program to clone or copy a list.   

# In[12]:


a=[10,20,30,40]
b=list(a)
print(b)


# ### 10. Write a Python program to find the list of words that are longer than n from a given list of  words.  

# In[14]:


a="The quick brown fox jumps over the lazy dog"
n=3
b=[]
txt=a.split(" ")
print(txt)
for  i in txt:
    if len(i)>3:
        b.append(i)
print(b)


# In[25]:


def abc(n,xyz):
    b=[]
    txt=xyz.split(" ")
    for i in txt:
        if len(i)>n:
            b.append(i)
    return b


# In[26]:


print(abc(4,"The quick brown fox jumps over the lazy dog"))


# ### 11. Write a Python function that takes two lists and returns True if they have at least one  common member.  
# 

# In[73]:


a=[10,20,30,40,50,60]
b=[70,80,90,100]
flag=0
for i in a:
    for j in b:
        if i==j:
            flag=1
    break
if flag==1:
    print("True")
else:
    print("False")
    
        


# In[42]:


def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
            return result  
#print(common_data([1,2,3,4,5], [5,6,7,8,9]))  
print(common_data([1,2,3,4,5], [5,6,7,8,9]))  


# In[43]:


def match(list,list1):
    result = False
    for i in list:
        for j in list1:
            if i==j:
                result = True
            return result


# In[44]:


print(match([1,2,3,4,5], [5,6,7,8,9]))  


# ### 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th  elements.

# In[52]:


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']  
b=[]
for i in range (len(color)):
    if i not in (0,4,5):
        #color.remove(i)
        #b.append(i)
        b.append(color[i])
print(b)


# ### 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 

# In[ ]:





# ### 14. Write a Python program to print the numbers of a specified list after removing even numbers  from it.  

# In[9]:


num = [7,8, 120, 25, 44, 20, 27] 
b=[]
for i in num:
    if (i%2!=0):
        #num.remove(i)
        b.append(i)
print(b)
#print(num)


# In[55]:


for i in range(len(num)+1):
    if num[i]%2==0:
        num.pop(i)
print(num)


# In[63]:


evenList = [11, 22, 31, 44, 51, 65, 71, 82, 91]
for ev in evenList:
    if (ev % 2 == 0):
        evenList.remove(ev)   
print(evenList)


# In[66]:


evenList = []

listNumber = int(input("Enter the Total List Items = "))
for i in range(1, listNumber + 1):
    listValue = int(input("Enter the %d List Item = " %i))
    evenList.append(listValue)

print("List Items = ", evenList)
i = 0

while (i < len(evenList)):
    if (evenList[i] % 2 == 0):
        evenList.remove(evenList[i])
    i = i + 1
    
print("List Items after removing even Items = ", evenList)


# ## 15. Write a Python program to shuffle and print a specified list. 

# In[76]:


from random import shuffle 
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']  
shuffle(color)  
print(color)  


# In[82]:


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
print(set(color))


# ### 16. Write a Python program to generate and print a list of first and last 5 elements where the  values are square of numbers between 1 and 30 (both included).  

# In[83]:


b=[]
for i in range(1,31):
    b.append(i*i)
print(b)


# In[84]:


b[:5]


# In[90]:


b[-5:]


# ## 17. Write a Python program to generate and print a list except for the first 5 elements, where the  values are square of numbers between 1 and 30 (both included).  
# 

# In[91]:


b=[]
for i in range(1,31):
    b.append(i*i)
print(b)


# In[92]:


b[6:]


# ## 19. Write a Python program to get the difference between the two lists.

# In[9]:


b=[]
while True:
    a=input("Enter a number")
    if a=="":
        break
    b.append(int(a))
print(b)

c=[]
while True:
    a=input("Enter a number")
    if a=="":
        break
    c.append(int(a))
print(c)

d=[]
for i in b:
    for j in c:
        d.append(i-j)
        break
print(d)


# In[11]:


list1 = [1, 3, 5, 7, 9] 
list2=[1, 2, 4, 6, 7, 8]  
diff_list1_list2 = list(set(list1) - set(list2))  
diff_list2_list1 = list(set(list2) - set(list1))  
total_diff = diff_list1_list2 + diff_list2_list1 
print(total_diff)  


# ### 20. Write a Python program access the index of a list.  
# 

# In[ ]:





# # 148. Write a Python program to remove specific words from a given list.  
#   
# Original list: 
# ['red', 'green', 'blue', 'white', 'black', 'orange']  
# Remove words:  
# ['white', 'orange']  
# After removing the specified words from the said list: 
# ['red', 'green', 'blue', 'black'] 
# 

# In[7]:


l= ['red', 'green', 'blue', 'white', 'black', 'orange']
l1=['white', 'orange']
for i in l1:
    l.remove(i)
print(l)


# In[9]:


l= ['red', 'green', 'blue', 'white', 'black', 'orange']
l1=['white', 'orange']

for i in l1:
    if i in l:
        l.remove(i)
print(l)


# In[10]:


l= ['red', 'green', 'blue', 'white', 'black', 'orange']
l1=['white', 'orange']
for i in l:
    if i=='white' or i=='orange':
        l.remove(i)
print(l)


# In[11]:


l= ['red', 'green', 'blue', 'white', 'black', 'orange']
l1=['white', 'orange']
for i in l1:
    a=l.index(i)
    l.pop(a)
    
print(l)


# #### 147. Write a Python program to interleave two given list into another list randomly.  
# Original lists: 
# [1, 2, 7, 8, 3, 7] 
# 
# [4, 3, 8, 9, 4, 3, 8, 9] 
# 
# Interleave two given list into another list randomly: 
# 
# [4, 1, 2, 3, 8, 9, 4, 3, 7, 8, 9, 8, 3, 7] 
# 

# In[1]:


a= [1, 2, 7, 8, 3, 7]
b=[4, 3, 8, 9, 4, 3, 8, 9]

for i in b:
    a.append(i)
print (a)


# In[4]:


import random
a= [1, 2, 7, 8, 3, 7]
b=[4, 3, 8, 9, 4, 3, 8, 9]

for i in b:
    c=random.choice(i)
print(c)


# In[8]:


x = [1, 2, 7, 8, 3, 7]
sum=1
for i in x:
    sum+=i
print(sum)
    


# In[22]:


b=[10,20,4,5,'b',70,'a']  
sum=0
for i in b:
    for n in str(i):
        if n.isdigit()==True:
            sum+=int(n)
print(sum)
        


# In[27]:


a="1234"
c=1
for i in range(len(a)-1):
    a[i]=a[i]+a[len(a)-c]
    a[len(a)-c]=a[i]-a[len(a)-c]
    a[i]=a[i]- a[len(a)-c]
    c+=1
print(a)
    
    


# In[28]:


a="1234"
print(a.reverse())


# #### 26. Write a python program to check whether two lists are circularly identical.  Solution:-  
# list1 = [10, 10, 0, 0, 10]  
# list2 = [10, 10, 10, 0, 0]  
# list3 = [1, 10, 10, 0, 0]  
# 

# ### 27. Write a Python program to find the second smallest number in a list.

# In[2]:


x = [1, 2, 7, 8, 3, 7]
y=set(x)
z=list(y)
print(z[1])


# In[ ]:




