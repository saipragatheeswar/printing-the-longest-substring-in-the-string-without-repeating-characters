#!/usr/bin/env python
# coding: utf-8

# In[1]:


#function to find max length list 

def maxi(lst):
    lst1=[]
    for i in lst:
        if len(lst1)<len(i):
            lst1=i

    return lst1

#funcction to perform longest substring in string without repeating character

def lss(x,dictionary):
    list1 =[]
    n=0
    for i in x:
        if i  in list1:
            dictionary.append(list1)
            b=0
            for j in list1:
                if i == j:
                    b1=b+1
                b+=1
            lss(x[b1:],dictionary)
            break
        list1.append(i)
        n+=1
        if n==len(x):
            dictionary.append(list1)
    return dictionary
 
#driver code

if __name__ == '__main__':
    x = "datascientist"
    dictionary = []
    z = lss(x,dictionary)
    x = maxi(z)
    print(x)


# In[ ]:




