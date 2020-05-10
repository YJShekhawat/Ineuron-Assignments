#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("this is my first program")


# In[8]:


x=[]
for i in range(2000,3200):
    if(i%5!=0):
           if(i%7==0):
                x.append(i)
print(x)


# In[2]:


firstname=input()
lastname=input()
name=firstname+" "+lastname
length=len(name)
while(length>=0):
    print(name[length-1])
    length=length-1


# In[12]:


diameter=12
pie=3.14
radius=diameter/2;
v=4/3*pie*pow(radius,3)
print("volume of sphere=",round(v,3),'cm\u00b3')


# In[ ]:





# In[10]:


s=input()
x=s.split(",")
list=[]
for i in x:
    list.append(int(i))
print(list)  


# In[4]:


k=4
for i in range(1,10):
    
    
    if i<6:
        
            
        for j in range(0,i):
       
            print("*",end="")
    
    else:
        
        
     
        for k in range(0,k):
            
            print("*",end="")
            
      
        
        
    print("\n")
    


# In[16]:


x=input()
print(x[::-1])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




