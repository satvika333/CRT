#!/usr/bin/env python
# coding: utf-8

# In[1]:


class abc:
    attribute1=10
    def display(self):
        print("this is in class")
obj=abc()
print(obj.attribute1)
obj.display()


# In[2]:


class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value
        print("the value is", value)
obj=abc(100)


# In[3]:


class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var
        print("the obj value is ",var)
        print("the class value is",abc.class_var)
obj1=abc(100)
obj2=abc(101)
obj3=abc(102)


# In[4]:


class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even= 1
    def even_odd(self, num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.even_odd(21)
         


# In[5]:


class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.even.append(num)
        else:
            number.odd.append(num)
n1=number(11)
n2=number(12)
n3=number(13)
n4=number(28)
n5=number(7)
print("even number list is",number.even)
print("odd number list is ",number.odd)


# In[6]:


class circle:
    pi=3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi*self.r*self.r
    def circum(self):
        return 2*circle.pi*self.r
c=circle(7.5)
print("area",c.area())
print("circumference",c.circum())


# In[ ]:


board=[['','',''],['','',''],['','','']]
def print_board(board):
    print(*board[0],sep="|")
    print("------")
    print(*board[1],sep="|")
    print("------")
    print(*board[2],sep="|")
def get_markers():
    marker1=input("player1 choice(X or O):").upper()
    marker2=""
    if marker1=="X":
        marker2='O'
        return['X','O']
    elif marker1=='O':
        marker2='X'
        return['O','X']
    else:
        print("Invalid Input")
        return get_markers()
def get_coordinates():
    x,y=list(map(int,input("enter the coordinates:").split()))
    if x in [0,1,2] and y in [0,1,2]:
        return[x,y]
    else:
        print("Invalid Input")
        return get_coordinates()
def check_for_win(board):
    for row in board:
        if row[0]==row[1] and row[1]==row[2] and row[1]!="":
            return True
    for i in range(len(board)):
        if board[0][1]==board[1][i] and board[1][i]==board[2][i] and board[2][i]!="":
            return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]!="":
        return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]!="":
        return True
    return False
def update_board(board,chance,marker,x,y):
    if chance==True:
        board[x][y]=marker
        if check_for_win(board):
            print("player 1 wins")
            return"game over"
        return False
    else:
        board[x][y]=marker
        if check_for_win(board):
            print("player2 wins")
            return"game over"
        return True
def play_game():
    player1=0
    player2=0
    m1,m2=get_markers()
    print(f"player1:{m1},player2:{m2}")
    chance=True
    while True:
        print_board(board)
        x,y=get_coordinates()
        if chance:
            chance=update_board(board,chance,m1,x,y)
            if chance=="game over":
                break
        else:
            chance=update_board(board,chance,m2,x,y)
            if chance=="game over":
                break
play_game()


# In[ ]:




