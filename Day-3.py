#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = 1
b = 5
a=b
b=a
print("Value of a:", a)
print("Value of b:", b)


# In[9]:


a=1
b=6
a=a+b
b=a-b
print("value of a:",a)
print("value of b:",b)


# In[10]:


a=11
b=22
print("before swap")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("after swap")
print("a=",a)
print("b=",b)


# In[14]:


a=20
b=22
print("before swap")
print("a=",a)
print("b=",b)
a=a*b
b=a//b
a=a//b
print("after swap")
print("a=",a)
print("b=",b)


# In[17]:


a=11
b=22
print("before swap")
print("a=",a)
print("b=",b)
a=a^b
b=a^b
a=a^b
print("after swap")
print("a=",a)
print("b=",b)


# In[35]:


num = [1,2,3,4,5,6,7,8,9,10]
print(num)
print("first element in the list",num[0])
print(num[2:5])
print(num[::2])
print(num[1::3])
del(num[2:4])
print(num)


# In[39]:


num =[1,'a',"abc", [2,3,4],5.6]
print(num)


# In[51]:


num = [100, 2, 3, 6, -8]
print(min(num))


# In[57]:


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(num))


# In[60]:


num = input()
print(int(num,17))


# In[61]:


num = [12, -2, -33, 84]
num.append(0)
print(num)
print(num.count(5))


# In[74]:


num = [6, 3, 7, 0, 1, 2, 4, 9]
num.insert(1,0)
print(num)


# In[78]:


num=[1,2,3,4,5,6,7]
num.remove(4)
print(num)


# In[81]:


num=[1,2,3,4,5,6,7]
num.reverse()
print(num)


# In[83]:


num=[1,2,3,4,5,6,7]
print(num.reverse())


# In[93]:


cubes=[]
for i in range(0,11):
    cubes.append(i**3)
print(cubes)


# In[106]:


n=int(input())
ne,p=0,0
while n!=0:
    a=n%10
    if a%2==0:
        p=p+a
    else:
        ne=ne+a
    n=n//10
print(p,ne)


# In[103]:


n=int(input())
ne,p=0,0
while n!=0:
    a=n%10
    if a%2==0:
        p=p+a
    else:
        ne=ne+a
    n=n//10
print(p,ne)


# In[108]:


num=[int(d) for d in str(input("enter number"))]
even,odd = 0,0
for i in range(0,len(num)):
    if i % 2 ==0:
        even =even + num[i]
    else:
        odd =odd + num[i]
print(abs(odd-even))


# In[109]:


cubes=[i**3 for i in range(11)]
print(cubes)


# In[110]:


print([i**3 for i in range(11)])


# In[120]:


term=int(input("enter the term:"))
if term%2 ==0:
    term=term//2
    print(3**(term-1))
else:
    term=term//2+1
    print(2**(term-1))
    


# In[10]:


term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(6*(term-1))
else:
    term=term//2*1
    print(7*(term-1))


# In[2]:


#0,0,7,6,14,12,21,18,27,24,..........
term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(6*(term-1))
else:
    term=term//2+1
    print(7*(term-1))


# In[8]:


val=int(input('enter the number:'))
x=0
y=0
for i in range(1,val+1):
    if(i%2!=0):
        x=x+7
    else:
        y=y+6
if(val%2!=0):
    print(' {} term in the program is {}'.format(val,x-7))
else:
     print('{} term in the program is {}'.format(val,y-6))


# In[18]:


#concatination of string
str1="india"
str1 += str2
print(str1)


# In[16]:


#repetition
str1 = "india"
print(str1 *10,)


# In[ ]:




