class Emp:
    def __init__(self,name,age,salary):
        self.name = name
        self.salary = salary
        self.age = age

    def __str__(self):
        print("Name : " ,self.name)
        print("Age: ", self.age)
        print("Salary : " ,self.salary)
        return ""

    def __add__(obj1,obj2):
        x = obj1.salary
        y = obj2.salary
        z= x + y
        e = Emp(obj1.name,obj1.age,z)
        return e

    def __gt__(obj1,obj2):
        x = obj1.age
        y = obj2.age
        if(x>y):
            return True
        else:
            return False


#def __gt__(str,n):
    #blank = " "
    #n = int(n)
    #leng =len(str)
    #str = blank*n + str
    #return str[0:leng]

   
e1 = Emp('Sumit',22,25000)
e2 = Emp('Sahay',21,21000)
e3 = Emp('Sumit Sahay',25,50000)
print(e1)
print(e2)
print(e3)
e4 = e1+e2+e3
print(e4)

if(e1>e2):
    print(e1.name," is senior")
else:
    print(e2.name," is senior")


#s1 = "Hello"
#print(s1 >3)
#print(s1<2)
