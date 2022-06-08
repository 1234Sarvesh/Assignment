#!/usr/bin/env python
# coding: utf-8

# In[1]:



num=int(input('Enter your age'))
if(num%5==0):
     print('Hello')
else:
     print('Bye')


# # Write a program to check whether a number is divisible by 7 or not.

# In[2]:


num=int(input('enter number '))

if(num%7 ==0):
    print('number divisible by 7')
else:
    print("number can't divisible by 7")


# # Write a program to check whether a person is eligible for voting or not. (accept age from user)

# In[6]:


age= int(input('Enter a Age'))
if(age<18):
    print("person is not eligible for voting ")
else:
    print("person is  eligible for voting")


# # Write a program to check whether a number entered by user is even or odd.

# In[7]:


num= int(input("Enter a Number"))
if(num % 2 == 0):
    print("Number is Even ")
else:
    print("Number is Odd ")
    


# ### Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
# First 100 units no charge Next 100 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs2000)

# In[8]:


unit = int(input("enter a electricity unit"))
if unit <= 100:
    print("no charge")
elif (unit > 100) and (unit<=200):
    unit = ((unit-100)*5)
    print("total bill is a ", unit)
elif (unit > 200):
    unit = ((unit-200)*10 + 500)
    print("total bill is a ", unit)
else:
    print("you enter a wrong value")


# ### Write a program to display the last digit of a number. (hint : any number % 10 will return the last digit)

# In[9]:


a= int(input(" Enter the Number: "))
b = a%10
print(b)


# # Write a program to accept percentage from the user and display the grade according to the following criteria:
# 
#   Marks                                    
#   
#   > 90    A
#   
#   
#   > 80 and <= 90   B
#   
#  
#   >= 60 and <= 80    C
#   
#   
#   below 60  D

# In[15]:


per = int(input('enter the per: '))
if(per>90):
    print('grade is A')
elif(per>80) and (per<=90):
    print('grade is B')
elif(per>=60) and (per<=80):
    print('grade is C')
else:
    print('grade is D')


# ##### Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
# 
#  Cost price (in Rs)        Tax
#  
#  > 100000                                                  15 %
#  
#  > 50000 and <= 100000                          10%
#  
#  <= 50000                                                  5%

# In[14]:


a=int(input('enter your bike price  '))
if(a>100000):
    onraod_price= (a* 0.15+a)
    print(onroad_price)
elif(a>50000 and a<=100000):
    onraod_price= (a*0.1+a)
    print(onraod_price)
elif(a<=50000):
    onroad_price=(a*0.05+a)
    print(onroad_price)
else:
    print("you entered wrong price")


# ### Write a program to check whether an years is leap year or not.

# In[16]:


year = int(input("Please Enter the Number you wish: "))

if (( year%400 == 0)or (( year%4 == 0 ) 
                      
    and ( year%100 != 0))):
    
    print("%d is a Leap year" %year)
else:
    print("%d is Not Leap Year" %year)


# ### Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

# In[19]:


Day= int(input("Please Enter the Day: "))
if(Day==1):
    print("Monday")
elif(Day==2):
    print("Tuesday")
elif(Day==3):
    print("Wednesday")
elif(Day==4):
    print("Thursday")
elif(Day==5):
    print("Friday")
elif(Day==6):
    print("Saturday") 
elif(Day==7):
    print("Sunday")    
else:
    print("Invalid")
    
    
    


# #### Write a program to check whether a number (accepted from user) is positive or negative.

# In[20]:


Num= int(input("Please Enter the Number: "))

if(Num>0):
    print("Number is positive")
else:
    print("Number is negative")


# #### Accept the age of 4 people and display the youngest one?

# ### Write a program to check a character is vowel or not.

# In[27]:


list = ['a','A','e','E','i','I','o','O','u','U']
b = input("Enter alphabate for find in the list")
if (b in list):
    print(b," alphabet is vowel")
else:
    print(" 'b' alphabet is consonant")


# #### Accept any city from the user and display monument of that city.
# 
#           City                                 Monument
#           
#           Delhi                               Red Fort
#           
#           Agra                                Taj Mahal
#           
#           Jaipur                              Jal Mahal

# In[6]:


city = input("Enter name of the city 1.Delhi 2.Agra 3.Jaipur")
if city=="Delhi":
    print("Monument name is : Red Fort")
elif city=="Agra":
    print("Monument name is : Taj Mahal")
elif city=="Jaipur":
    print("Monument name is : Jal Mahal")
else:
     print("Enter correct name of city")


# #### Write a program to check whether a person is senior citizen or not.# 

# In[2]:


age= int(input('Enter a Age'))
if(age>=60):
    print("person is senior citizen ")
else:
    print("person is not senior citizen ")


# #### Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

# In[4]:


num= int(input("Enter a Number"))
if(num % 2 == 0) and (num % 3 == 0):
    print("Number is divisible by 2 and 3 ")
else:
    print("Number is not divisible by 2 and 3  ")


# ##### Accept the age of 4 people and display the youngest one?

# In[15]:


a = int(input("Enter the age of person A"))
b = int(input("Enter the age of person B"))
c = int(input("Enter the age of person C"))
d = int(input("Enter the age of person D"))
        
if(a<b and a<c and a<d):
    print("A is youngest one")
    
elif(b<a and b<c and b<d):
    print("A is youngest one")
    
elif(c<a and c<b and c<d):
    print("A is youngest one")   
    
else:
    print("D is youngest one")
    


# ##### Accept the following from the user and calculate the percentage of class attended:
# a. Total number of working days
# 
# b. Total number of days for absent
# 
# After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam.

# In[26]:


a=int(input("Total Number of working days:"))

b=int(input("Number of days absent:"))

percentage=a-b/a*100

print(percentage)

if percentage>=75:

        print("The student is allowed to sit in the exam hall")

else:

        print("The student is not allowed to sit in the exam hall")
        


# ### Accept three sides of triangle and check whether the triangle is possible or not.
# (triangle is possible only when sum of any two sides is greater than 3rd side)

# In[29]:


a= int(input())
b= int(input())
c= int(input())

if(a + b > c and a + c > b and b + c > a):
    print(" Valid Triangle")
else:
    print("Invalid Triangle")


# #### Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
# Note :
# 
# An equilateral triangle is a triangle in which all three sides are equal.
# 
# A scalene triangle is a triangle that has three unequal sides.
# 
# An isosceles triangle is a triangle with (at least) two equal sides.

# In[30]:


a= int(input())
b= int(input())
c= int(input())
if a==b==c:
    print("It is equilateral triangle")
elif a!=b!=c:
    print("It is scalene triangle")
else:
    print("It is  isosceles triangle")


# #### Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly
# Age Sex Wage/day
# 
# =18 and <30 M 700 F 750 =30 and <=40 M 800 F 850

# In[45]:


a= int(input("Enter age:"))
b= input("Enter Gender:")
c= int(input("Enter  Working Days:"))

if(a>=18 and a<=30 and b=="M"):
    wages = c *700  
    print("Person will recive: ", wages)
    
elif(a>=18 and a<=30 and b=="F"):
    wages = c * 750
    print("Person will recive : ", wages)
    
elif(a>=40 and b=="M"):
    wages = c * 800
    print("Person will recive : ", wages)  
        
else:
    wages = c * 850
    print("Person will recive : ", wages) 
    

    
    
       


# In[ ]:




