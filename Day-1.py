#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input())
if (n>21):
    print(n-21)
elif n<21:
    print(21-n)
else :
    print('0')


# In[11]:


a=int(input("enter a:"))
b=int(input("enter b:"))
c=a//b
d=a/b
e=a**b
print(c,d,e)


# In[12]:


x=5
y=3
print(x+y) addition 8
print(x-y) subtraction 2
print(x*y) multiplication 15
print(x//y) floor division 1
print(x/y) division 1.666666666667
print(x**y) exponentiation 125
print(x%y) moulus 2


# (>) greater than 
# (<=) less than or equal to
# (=) equal to
# (!=) not equal to
# (>=) greater than or equal to
# (<) less than
# (

# In[21]:


a=5
b=5.0
if a==b:
    print("true")


# In[32]:


a=5
a+=10
print(a)
a-=10
print(a)
a*=5
print(a)
a//=5
print(a)
a-=5
print(a)
a//=5
print(a)
a**=2
print(a)
a


# In[44]:


a=10
b=5
c=a & b
d=a | b
e=~(a ^ b)
f= ~-555
g=a<<4
print(c)
print(d)
print(e)
print(f)
print(g)


# In[39]:


50>>3


# In[40]:


60>>2


# In[45]:


20>>2 divide


# In[46]:


20<<2 multiply


# In[51]:


a=1000
b=1500
c=-500
d=4000
print(a<b and a<c and a>d)


# In[53]:


a=1000
b=1500
c=-500
d=4000
e=2000
n=[a,b,c,d,e]
print(min(n))


# In[63]:


a=5
b=10
c=15
print(a if (a<b and a<c)else b if b<c else c )


# In[1]:


a=5
b=10
c=15
if(a>b and a>c):
    print(a)
elif b>c:
    print(b)
else:
    print(c)


# In[57]:


a=5
b=10
print(a if a>b else b)


# In[ ]:




