#!/usr/bin/env python
# coding: utf-8

# ## Dot Matrix display

# #### This project aims to be capable of producing outputs for dot matix  LCD displays. At least by demonstrating the underlying logic along the way:

# ##### Create an array for each text symbol to form an element:

# In[ ]:


arr = ['','','']
arr


# #### Each element has been left blank, and may be filled, using '_' as a visual version of ' '.
# #### So each element be have the default value of '_'

# In[ ]:


arr = ['_','_','_']
arr


# #### There won't be much scope for displaying charactors in a 1D array, lets form several layers to our display:

# In[ ]:





# In[ ]:


cols = 3
lyr = [arr for line in range(cols)]
lyr


# #### To be selective with our element:
# #### The central column = '0'

# In[ ]:


lyr[0][1]  = '0'
lyr


# #### The output does not look to realistic.
# #### Let's create an object 'lines' for each layer to join onto:
# #### for lin in (1,2,3), the element of lines will be the layer (lyr) joined

# In[ ]:


lines = ["" for lin in range(3)]
for lin in range(3):
    lines[lin] += "".join(lyr[lin])+''


# #### Then a for loop to run through each line and print
# 

# In[ ]:


for lin in lines:
    print(lin)


# #### That's the middle column filled, how about some variety:
# #### Let's create a diagonal:
# #### First we must create another for loop, such that each row of the input matrix is created sequentially:
# #### line 7: define the array explicity (not as the variable)

# 

# In[ ]:


arr = ['_','_','_']
elem = '*'
cols = 3

for i in range(cols):
    lines = [""for lin in range(cols)]
    lyr = [['_','_','_'] for line in range(cols)]
#    lyr = [arr for line in range(cols)]

    lyr[0][0]=elem
    lyr[1][1]=elem
    lyr[2][2]=elem

    #lines = ["" for lin in range(3)]
for lin in range(cols):
    lines[lin] += "".join(lyr[lin])+''

for lin in lines:
    print(lin)


# #### Or a box:

# In[ ]:


#arr = ['_','_','_']
elem = '*'
cols = 3

for i in range(cols):
    lines = [""for lin in range(cols)]
    lyr = [['_','_','_'] for line in range(cols)]
#    lyr = [arr for line in range(cols)]
#top row:
    lyr[0][0]=elem
    lyr[0][1]=elem
    lyr[0][2]=elem
# middle row:
    lyr[1][0]=elem
#   lyr[1][1]= elem
    lyr[1][2]=elem
# bottom row:
    lyr[2][0]=elem
    lyr[2][1]=elem
    lyr[2][2]=elem
    
    

    #lines = ["" for lin in range(3)]
for lin in range(cols):
    lines[lin] += "".join(lyr[lin])+''

for lin in lines:
    print(lin)


# #### Let's expand the dot matrix, setting cols as a cofactor of the lyr (line 7) and redefine variable to 5.

# In[ ]:


cols=5
elem = '0'


for i in range(cols):
    lines = [""for lin in range(cols)]
    lyr = [cols*['_'] for line in range(cols)]
    
    
    

#    lyr = [arr for line in range(cols)]    
#lines = ["" for lin in range(3)]
for lin in range(cols):
    lines[lin] += "".join(lyr[lin])+''

for lin in lines:
    print(lin)


# ##### The next challenge being getting the lyr components to expand in relation to the new scale.
# ##### To acheive this the number of column will equal number of rows, a square matrix.
# ##### Another for loop will iterate through each row and column position and assign the elem = '*'.

# In[ ]:


cols=20
elem = '*'


for i in range(cols):
    lines = [""for lin in range(cols)]
    lyr = [cols*[' '] for line in range(cols)]
#top row:
i=j = cols

for i in range(cols):
    for j in range(cols):
        lyr[i][j]='*'

#    lyr = [arr for line in range(cols)]    
#lines = ["" for lin in range(3)]
for lin in range(cols):
    lines[lin] += "".join(lyr[lin])+''

for lin in lines:
    print(lin)


# ##### To create a box, be specific where to assign the elem

# In[11]:


cols=20
elem = '0'


for i in range(cols):
    lines = [""for lin in range(cols)]
    lyr = [cols*[' '] for line in range(cols)]
#top row:
i=j = cols

for i in range(cols):
    for j in range(cols):
        if i  == cols-1 or i == 0:
            lyr[i][j]='*'
        if j  == cols-1 or j == 0:
            lyr[i][j]='*'
        

    
#    lyr = [arr for line in range(cols)]    
#lines = ["" for lin in range(3)]
for lin in range(cols):
    lines[lin] += "".join(lyr[lin])+''

for lin in lines:
    print(lin)


# ##### We can create iterative patterns based upon the logic built into the for loop on line 11:

# In[13]:


cols=20
elem = '0'


for i in range(cols):
    lines = [""for lin in range(cols)]
    lyr = [cols*[' '] for line in range(cols)]
#top row:
i=j = cols

for i in range(cols):
    for j in range(cols):
        if i%5 == 0:
            lyr[i][j]='*'
        if j %5 == 0:
            lyr[i][j]='.'
        

    
#    lyr = [arr for line in range(cols)]    
#lines = ["" for lin in range(3)]
for lin in range(cols):
    lines[lin] += "".join(lyr[lin])+''

for lin in lines:
    print(lin)


# In[12]:


cols=25
elem = '*'


for i in range(cols):
    lines = [""for lin in range(cols)]
    lyr = [cols*[' '] for line in range(cols)]
#top row:
i=j = cols

for i in range(cols):
    for j in range(cols):
        if i%5 == 0 or j%3 == 0:
            lyr[i][j]='*'
        if j %5 == 0 or i%3 ==0:
            lyr[i][j]='.'
        

    
#    lyr = [arr for line in range(cols)]    
#lines = ["" for lin in range(3)]
for lin in range(cols):
    lines[lin] += "".join(lyr[lin])+''

for lin in lines:
    print(lin)


# In[ ]:





# In[ ]:




