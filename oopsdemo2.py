class emp :
    count = 0
    def __init__(self,name,age,salary,desg):  #constructor
        self.name = name
        self.age = age
        self.salary = salary
        self.desg = desg
        emp.count+=1

    #def __init__(self,name,age):  #overloaded constructor not allowed...
     #  self.name = name
     #  self.age = age
     #  emp.count+=1



     #Overloading not allowed ...We can mention functions with same name
     #and different parameters but only the last method/const. will be considered
     #...hence..no use!!

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        print("Designation: ",self.desg)

    def set_age(self,age):
        self.age = age

    def __del__(self):         #destructor
        print("Object with name  : '%s' getting destroyed"%self.name)


e1 = emp("Sumit",21,54000,"Programmer")
e1.display()
print("------------------------------")
e2 = emp("Sahay",21,50000,"Programmer")
#e2.count = 5
#print(e2.count)
e2.set_age(20)
e2.display()

print("\nTotal no. of employees created: ",emp.count)

del e1
del e2

#print(e1.name)
