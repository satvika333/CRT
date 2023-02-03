#!/usr/bin/env python
# coding: utf-8

# # DAY-4

# In[4]:


#repetition
str1 = "india"
print(str1 *10,)


# In[9]:


text ='india'
index = 0
for i in text:
    print("text[", index,"]= ",i)
index += 1


# In[11]:


text = "india is great"
print(text.title())


# In[13]:


text = "India Is Great"
print(text.swapcase())


# In[20]:


text = "India Is Great"
print(text.split())


# In[21]:


print('-'.join(['India','Is','Great']))


# In[44]:


str1 = '66'
print(str1.zfill(4))


# In[1]:


str= 'satvika'
print(str.upper())


# In[43]:


str= 'SATVIKA'
print(str.lower())


# In[3]:


import string
print(string.digits)


# In[11]:


import string
ch = 'g'
print('a' <=ch <= 'z')


# In[16]:


str1= "hello"
print(dir(str1))


# In[19]:


import re
str1 = "she sells sea shells at sea shore "
p1= "sells"
if re.match(p1,str1):
    print("match not found")
else:
    print(p1, "not present in string")
p2= "she"
if re.match(p2,str1):
    print("match found")
else:
    print(p2, "not present in string")


# In[20]:


import re
str1 = "she sells sea shells at sea shore "
p1= "sells"
if re.match(p1,str1):
    print("match not found")
else:
    print(p1, "not present in string")


# In[21]:


import re
str1 = "she sells sea shells at sea shore "
p1= "sea"
rep = 'ocean'
ns= re.sub(p1, rep, str1, 1)
print(ns)


# In[26]:


#write a program to find one vowel from the string
import re
p= r"[aeiou]"
if re.search(p,"clue"):
    print("matchy vowel")


# In[27]:


import re
p= r"[bcdfghjklmnpqrstvxyz]"
if re.search(p,"clue"):
    print("matchy consonants")


# In[38]:


#0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8,.......
n=int(input("enter the term:"))
if n%2==0:
    n=n//2
    print(1*(n-1))
else:
    n=n//2+1
    print(2*(n-1))


# In[39]:


#0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8,.......
n=int(input("enter the term:"))
if n%2==0:
    n=n//2
    print(1*(n-1))
else:
    n=n//2+1
    print(2*(n-1))


# In[50]:


size=int(input("enter the size of bin:"))
max=count=flag=0
x=input()
arr=list(x)
for i in range(0, size):
    if arr[i]=='1':
        count = count+1;
        flag= 1;
    elif (arr[i]=='0' and flag==1):
            count=0
            flag=0
    if count >max:
        max=count
print(max)
            


# In[ ]:




