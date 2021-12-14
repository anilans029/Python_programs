#!/usr/bin/env python
# coding: utf-8

# # Pattern 1
# 

# In[1]:


n = int(input("enter the no.of rows:"))
for i in range(n):
    for j in range(0,i+1):
        print("* ", end ="")
    print("\r")


# 
# # Pattern2

# In[2]:


n = int(input("enter no.of rows:"))
k =1
for i in range(n):
    for j in range(k):
        print("*",end = "")
    k += 2
    print("\r")
print()   
for i in range(n):
    for j in range(2*i+1):
        print("*", end ="")
    print("\r")


# # Pattern 3

# In[3]:


n = int(input("enter the no.of rows:"))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end = "")
    for j in range(2*i+1):
        # for j in range(2*i+1):// here we can print pyramid in the form 1 star,2 star,3star also by 
        print("*",end = "")
        
    print("\r")


# # Pattern 4
# same above program without using for loop

# In[4]:


n = int(input("enter the no.of rows:"))
i=0
while(i<n):
    print(" "*(n-i)+"* "*(i+1))
    i+=1
i=0
while(i<n):
    print(" "*(n-i)+"*"*(2*i+1))
    i+=1


# # Pattern 5

# In[5]:


n = int(input("enter the no.of rows:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end ="")
    for j in range(i):
        print("* ",end ="")
    print("\r")


# # Pattern 6

# In[6]:


n = int(input("enter the no.of rows:"))
i=0
while(i<n):
    print(" "*(n-i-1)+"* "*(i+1))
    i+=1
i=1
while(i<n):
    print(" "*(i)+"* "*(n-i))
    i+=1    


# # Pattern 6

# In[7]:


n = int(input("enter the no.of rows:"))
for i in range(n,0,-1):
    for j in range(i):
        print("* ",end="")
    print("\r")


# # Pattern7

# In[8]:


for i in range(8):
    for j in range(5):
        if ((j==0 or j==4)and i!= 0)or ((i==0 or i == 4) and(j>0 and j<4)):
            print("* ",end ="")
        else:
            print(end="  ")
    print()
        
                                         


# # Pattern 8

# In[9]:


for i in range(9):
    for j in range(5):
        if((j==0 or j==4)and(i!=0 and i!= 8 and i!=4)) or ((i ==0 or i==8 or i== 4)and(j!=4)):
            print("* ",end="")
        else:
            print(end="  ")
    print("\r")


# # Pattern 9

# In[10]:


for i in range(8):
    for j in range(5):
        if((j==0) and (i!= 0 and i!= 7)) or ((i==0 or i== 7) and (j!= 0)):
            print("* ",end ="")
        else:
            print(end =" ")
    print("\r")


# # Pattern 9

# In[11]:


for i in range(8):
    for j in range(5):
        if((j ==0 or j == 4)and (i!= 0 and i!=7)) or ((i == 0 or i== 7)and(j!=4)):
            print("* ", end ="")
        else:
            print(end="  ")
    print()


# # Pattern 10

# In[12]:


for i in range(7):
    for j in range(5):
        if (j ==0) or (i == 0 or i == 3 or i ==6):
            print("* ", end="")
        else:
            print(end ="  ")
    print()


# # Pattern 11

# In[13]:


for i in range(8):
    for j in range(5):
        if(j ==0) or (i == 0 or i == 4):
            print("* ", end = "")
        else:
            print(end = "  ")
    print()


# # Pattern 12

# In[14]:


for i in range(7):
    for j in range(6):
        if(( j == 0)or ( j==4 and i>3)) or ((i==0and j<5) or (i==6 and j<5) or(i ==3 and j>2)):
            print("* ", end = "")
        else:
            print(end ="  ")
    print()


# # Pattern 13

# In[15]:


for i in range(8):
    for j in range(5):
        if(j == 0 or j == 4) or ( i == 4 ):
            print("* ", end = "")
        else:
            print(end="  ")
    print()


# # Pattern 14

# In[16]:


for i in range(8):
    for j in range(5):
        if (j == 2) or (i == 0 or i == 7):
            print("* ", end ="")
        else:
            print(end ="  ")
    print()


# # Pattern 15

# In[17]:


for i in range(8):
    for j in range(5):
        if (j ==2 or (j == 0 and i> 4)) or (i ==0 or ((i == 7 or i ==5)and (j <3))):
            print("* ", end= "")
        else:
            print(end ="  ")
    print()


# # Pattern 16

# In[18]:


a = 0
b = 4

for i in range(7):
    for j in range(5):
        if (j == 0) or (i == j + 2):
            print("* ", end = "")
        elif (i == a and j == b) and (j >1):
            print("* ", end = "")
            a += 1
            b -= 1
        else:
            print(end = "  ")
    print()
        


# # Pattern 17

# In[19]:


for i in range(8):
    for j in range(5):
        if j == 0 or (i ==7 and j>0):
            print("* ", end = "")
        else:
            print(end = "  ")
    print()


# # Pattern 18

# In[30]:


for i in range(8):
    for j in range(7):
        if j == 0 or j==6 or (i == 1 and j == 5) or (i == 2 and j == 4):
            print("* ", end = "")
        elif i ==j and j<4:
             print("* ", end = "")
        else:
            print(end ="  ")
    print()


# # Pattern 19
# 

# In[35]:


for i in range(6):
    for j in range(6):
        if (j == 0 or j == 5) or i == j:
            print("* ", end = "")
        else :
            print(end ="  ")
    print()


# # Pattern 20

# In[41]:


for i in range(6):
    for j in range(5):
        if ((j == 0 or j == 4) and (i!= 0 and i!= 5)) or ((i == 0 or i == 5) and (j>0 and j < 4)):
            print("* ", end = "")
        else:
            print(end ="  ")
    print()


# # Pattern 21

# In[49]:


for i in range(7):
    for j in range(5):
        if ((j == 0 )or (j==4 and  (i != 0 and i< 3))) or ((i == 0 or i == 3) and (j != 4)):
            print("* ", end ="")
        else:
            print(end = "  ")
    print()


# # Pattern 22

# In[56]:


for i in range(7):
    for j in range(6):
        if ((j==0 or j==5) and (i!=0 and i< 5)) or (i== 0 or i== 5)and ((j!=0 and j!=5)):
            print("* ", end ="")
        elif (i == 4 and j ==1) or (i == 6 and j == 4):
             print("* ", end ="")

        else:
            print(end ="  ")
    print()


# # Pattern 23

# In[61]:


for i in range(7):
    for j in range(5):
        if ((j == 0 or j == 4)and (i!= 0 and i!= 3)) or ((i==0 or i==3)and (j!= 4)):
            print("* ", end = "")
        else:
            print(end = "  ")
    print()


# # Pattern 24

# In[74]:


for i in range(7):
    for j in range(5):
        if (((j==0 and i<3)or(j==4 and i>3))and(i!=0 and i!=6))  :
            print("* ",end = "")
        elif (i == 0 or i == 3 or i == 6) and j!= 0 and j != 4:
            print("* ",end = "")
        else:
            print(end ="  ")
    print()


# # Pattern 25

# In[76]:


for i in range(6):
    for j in range(5):
        if (j == 2) or i == 0:
            print("* ", end = "")
        else:
            print(end ="  ")
    print()


# # Pattern 26

# In[82]:


for i in range(6):
    for j in range(5):
        if ((j==0 or j==4) and i != 5) or i==5 and (j !=0 and j!= 4):
            print("* ", end = "")
        else:
            print(end = "  ")
    print()


# # Pattern 27

# In[92]:


row = 0
col = 6
for i in range(4):
    for j in range(7):
        if i == j:
            print("* ",end = "")
        elif row == i and col == j:
            print("* ",end = "") 
            row += 1
            col -= 1
        else:
            print(end ="  ")
    print()


# # Pattern 28

# In[97]:


row = 1 
col =2
for i in range(4):
    for j in range(7):
        if (j == 0 or j == 6) or i == j-3:
            print("* ",end = "")
        elif row == i and col == j:
            print("* ",end = "")
            row += 1
            col -= 1
        else: 
            print(end ="  ")
    print()


# # Pattern 29 

# In[100]:


row = 0
col =4
for i in range(5):
    for j in range(5):
        if i==j and i!=2:
            print("* ", end ="" )
        elif row == i and col ==j:
            print("* ", end ="" )
            row += 1
            col -= 1
        else: 
            print(end = "  ")
    print()


# # Pattern 30

# In[104]:


row = 0
col =4
for i in range(5):
    for j in range(5):
        if (j == 2 and i>1) or (i==j and i <2) or():
            print("* ", end ="")
        elif row ==i and col == j:
            print("* ", end ="")
            row += 1
            col -=1
        else:
            print(end ="  ")
    print()


# # Pattern 31

# In[107]:


for i in range(5):
    for j in range(5):
        if j ==4 or i ==j or i ==0 :
            print("* ", end ="")
        else: 
            print(end ="  ")
    print()


# # Pattern 32

# In[112]:


row = 1
col =3
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4:
            print("* ", end="")
        elif row == i and col ==j :
            print("* ", end="")
            row += 1
            col  -= 1
        else:
            print(end ="  ")
    print()


# # Pattern 33 Floyd's Triangle

# In[122]:


n = int(input("enter the no.of rows:"))
num =1
for i in range(n):
    for j in range(i+1):
        print(num, end = " ")
        num += 1
    print()


# # Pattern 34

# In[126]:


n = int(input("enter the no.of rows: "))
st = "PYTHON"
for i in range(n):
    for j in range(i+1):
        print(st[j],end =" ")
    else: 
        print(end = "  ")
    print()


# In[127]:


1+2


# # Pattern 35

# In[134]:


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end =" ")
    print()
print()
    
for i in range(5,0,-1):
    for j in range(i):
        print(i, end = " ")
    print()
        


# # Pattern 36

# In[149]:


row = 1 ;col = 2
for i in range(4):
    for j in range(7):
        if i== j - 3 or i == 3:
            print("* ", end = "")
        elif row == i and col == j:
            print("* ", end = "")
            row += 1
            col -= 1
        else:
            print(end ="  ")
    print()
print()

row_2 =1
col_2 = 2
for i in range(4):
    for j in range(7):
        if i == j-3 or (i == 3 and j%2==0) :
            print("* ",end = "")
        elif row_2 == i and col_2 == j :
            print("* ",end = "")
            row_2+= 1
            col_2 -= 1
        else: 
            print(end = "  ")
    print()
    


# #  Pattern 37

# In[153]:


for i in range(4):
    for j in range(i+1):
        print("* ", end = "")
    print()
    
print()

n = int(input("enter the no.of rows: "))
row = 0
while(row < n):
    col =0
    while(col< row+1):
        print("* ", end = "")
        col+=1
    print()
    row += 1


# # Pattern 38

# In[163]:


n = int(input("enter the no.of rows: "))
for i in range(n):
    for j in range(n-1-i,0,-1):
        print(end= " ")
    for j in range(i+1):
        print("* ",end ="")
    print()

print()

i =0
while(i<n):
    j =0
    while(n-i-1 > j):
        j+= 1
        print(end =" ")
    j =0
    while(j < i+1):
        print("* ", end ="")
        j+=1
    i += 1
    print()
        


# #  Python 39

# In[172]:


# import math
# n = int(input("enter the no.of rows: "))
# row = 1
# col =(math.ceil((2*n -1)/2))-2

# for i in range(n):
#     for j in range(2*n-1):
#         if i == j-((math.ceil((2*n -1)/2))-1):
#             print("* ", end = "")
#         elif j == col and i == row:
#             print("* ", end = "")
#             row +=1
#             col-= 1
#         else: print(end ="  ")
#     print()

for i in range(5):
    for j in range(5):
        if i + j == 2 or j-i ==2 or i -j ==2 or i+j == 6:
            print("* ", end="")
        else:
            print(end ="  ")
    print()


# In[177]:


row = 2
col = 6
for i in range(6):
    for j in range(7):
        if (i==0 and j %3 != 0) or (i ==1 and j %3 ==0) or(i -j ==2):
            print("* ",end ="")
        elif i == row and col == j:
            print("* ",end ="")
            row +=1
            col -= 1
        else:
            print(end ="  ")
    print()


# In[ ]:




