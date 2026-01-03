# import array as arr
from array import *

val=array('d',[1,2,3,4,5,6,7,8,9.5])

for i in range(0,len(val)):
  print(val[i], end=" ")

print('\n')

for x in val:
  print(x,end=",")

print('\n')
print(val.typecode)

val.reverse()

for i in range(0,len(val)):
  print(val[i], end=" ")

val.insert(1,10.5)
val.append(100)
val[2]=50.5

copyArray=array(val.typecode, (x for x in val))

copyArray.pop(3) #if inxex not given last eleemnt will be deleted

copyArray.remove(15) #to remove by element value

a=val[2:5] #slicing,  end index is excluded in slicing
a=val[2:-3] #slicing, negative index
a=val[::-1] #reversing using slicing


# for i in range(0,len(copyArray)):
#   print(copyArray[i], end=" ")


#taking input from the user

arr=array('i',[])

n=int(input("Enter number of elements: "))

for i in range(0,n):
  arr.append(int(input("Enter element: ")))

for x in arr:
  print(x,end=" ")

#searching in a array
arr=array('i',[25,56,66,662,45])

i=arr.index(45)
print(i)

