import math

def perfect_sqrt(list1):
    count = 0
    for num in list1:
          val=math.sqrt(num)
          if (val - int(val) == 0) :
              print("perfect square:",num)
              count+=1
    if(count==0):
        print("No perfect square root found")


#func call
list1 = [];
print("Enter any 10 numbers..")
for i in range(1,11):
        num= int(input("Enter number:"))
        list1.extend([num])
print("------------------------")
perfect_sqrt(list1);
    
    
