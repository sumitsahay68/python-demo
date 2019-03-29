from array import *
from numpy import *

arr =  array([1,2,3,4,5.0,78,3],str)
print(arr)
print(arr.dtype)
print(type(arr))


ls  = linspace(1,10,20) #3rd arg is 50 by default
print(ls)
print()
logs =  logspace(1,50,5)
print("%.1f"%logs[2])
print()

x = arange(1,500,0.695)
print(x)
print()

z = zeros(90,int)  #default is float
print(z)

o = ones(85,int)    #default is float
print(o)

o1 = ones(85,bool)    #default is float
print(o1)

print("-------------")

print("--Deep Copying--")
arr0 = arr.copy()
arr0[0] ='hey'
print(arr,":",id(arr))
print(arr0,":",id(arr0))
print()
print("--Shallow Copying--")
arr1 = arr.view()
arr1[0] ='hey'
print(arr,":",id(arr))
print(arr1,":",id(arr1))
