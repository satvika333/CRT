#!/usr/bin/env python
# coding: utf-8

# In[7]:


a,b,c=10,20,30
print(b,c,a,sep='?')
print('9','12','2016',sep='-')
print("A","B","C",sep='%')


# In[22]:


apple=100
banana=200
pineapple=300 
print(apple,end='* ')
print(banana,end='- ')
print(pineapple,end='? ')

print(apple,banana,pineapple)


# In[32]:


x, y, z = input("Enter a three value:").split('*')
print("Total number of students: ", x)
print("Number of boys is:", y)
print("Number of girls is:", z)
      


# In[7]:


x, y, z = input("Enter a three value:").split('0')
print("Total number of students: ", x)
print("Number of boys is:", y)
print("Number of boys is:", z)


# In[2]:


email="satvika@gmail.com"
pwd=123456
cemail=input("enter the email:")
cpwd=int(input("enter the pwd:"))
if(email==cemail and pwd==cpwd):
    print("login successfully")
elif(email==cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
     print("login failed due to pwd")
else:
     print("login failed due to email and pwd")

    


# In[3]:


a=5
b=5.0
if(a==b):
    print("yes")
else:
    print("no")


# In[5]:


a=5
b=1
if(1==b):
    print("yes")
else:
    print("no")


# In[7]:


a=int(input("enter a value:"))
if(a%7==0):
    print("divisible")
else:
    print("not divisible")


# In[2]:


email="satvika@gmail.com"
pwd=123456
otp=5076
cemail=input("enter the email:")
cpwd=int(input("enter the pwd:"))
cotp=int(input("enter the otp:"))
if(email==cemail and pwd==cpwd and otp==cotp):
    print("login successfully")
    if(cotp==otp):
        print("your order is placed successfully")
    else:
        print("order failed")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
     print("login failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
     print("login failed due to email and pwd")

    


# In[6]:


a="balaji"
print('y' not in a)
print('y' in a)
print(a[3])


# In[12]:


for i in range(1,10):
    print(i,end='*')


# In[20]:


for i in range(10,0,-1):
    print(i,end='*')


# In[12]:


for i in range(97,122):
    print(chr(i),end=" ")


# In[18]:


for i in range(65,91):
    print(chr(i),end=" ")


# In[22]:


for i in range(65,91):
    if(i==65 or i==69 or i==73 or i==79 or i==85):
        print(chr(i),end=" ")

    


# In[27]:


for i in range(122,96,-1):
        print(chr(i),end=" ")
    


# In[28]:


for i in range(65,91):
    if(i==65 or i==69 or i==73 or i==79 or i==85):
        print(chr(i),end=" ")

    


# In[29]:


for i in range(90,64,-2):
    if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
        print(chr(i),end="")


# In[1]:


d,c,m=list(map(int,input().split()))
data=float(input())
if 84>=d and c<=3000 and  100>=m and  2>=data: 
    print(84-d)
    print(3000-c)
    print(100-m)
    print(2-data)
else:
    print("your plan is expired")


# In[3]:


d,c,m=list(map(int,input().split()))
data=float(input())
if 84>=d:
    print(84-d)
    if c<=3000:
        print(3000-c)
        if 100>=m:
            print(100-m)
            if 2>=data:
                print(2-data)
else:
    print("your plan is expired")


# In[2]:


d,c,m=list(map(int,input().split()))
data=float(input())
if 84>=d:
    print(84-d)
    if c<=3000:
        print(3000-c)
        if 100>=m:
            print(100-m)
            if 2>=data:
                print(2-data)
else:
    print("your plan is expired")


# In[2]:


for i in range(1,151):
    if i%10==0:
        print(i)


# In[6]:


for i in range(0,51,5):
    print(i)


# In[7]:


for i in range(0,51,5):
    if i%10!=0:
        print(i)


# In[8]:


for i in range(1,6,2):
    print(i*5)


# In[9]:


for i in range(1,30):
    if(i%2==1 and i<=5):
        print(i*5)


# In[20]:


for i in range(-10,0,2):
    print(i)


# In[32]:


n=int(input())
for i in range(n):
    
    for j in range(0,i):
        print('*',end=' ')
    print(' ')


# In[39]:


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print("\n")


# In[44]:


for i in range(97,123):
    for j in range(97,i+1):
        print(chr(i),end="")
    print("\n")


# In[45]:


for i in range(97,123,2):
    for j in range(97,i+1):
        print(chr(i),end="")
    print("\n")


# In[46]:





# In[50]:


for i in range(1,11):
    print(i*5)


# In[54]:


for i in range(1,11):
    print(i,"*5=",i*5)


# In[2]:


i=int(input())
while(i<=5):
    while(j<=i):
        print("*",end="")
        j=j+1
    i=i+1
    print("\n")
        


# In[ ]:


i=1

