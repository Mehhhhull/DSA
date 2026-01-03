# import numpy as np
from numpy import *

#val=array([1,2,6.9],float)also cn typecast if possible
val=linspace(10,20,5)
# will divide in 5 equal parts, 10 and 20  both included
val=arange(10,20,2) #20 isnt included
val=logspace(10,20,2)
val=zeros(10)
val=full(10,5) #size 10 nd all 5
#using numpy you can save diff types of elements in array-Hetrogenous






zero=array(10)
print(zero)

one=array([1,2,3,4,5,6])
print(one)

two=array([[1,2,3],[4,5,6],[7,8,9]]) #3 x 3 2darray

thrree=array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(thrree) 