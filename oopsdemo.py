class Emp:
    #name  = "Sumit"  #static by default withot 'self'
    #age = 21
    def __init__(self,name="Sumit",age = 21):
        self.name = name
        self.age = age
    def display():
        print("Object Oriented Programming")
    def display_inst(self):
        print("Instance OOPS")
        print("Name  : ",self.name)
        print("Age : ",self.age)

e1 = Emp()
e2 = Emp("Sahay",21)
Emp.display() #by default static i.e. belonging to class
e1.display_inst()
Emp.display_inst(e2)


print("-------------------------------")

class Calculator:
    def add(self,a,b):
        print("Add Result: ",(a+b))


c1 = Calculator()
c1.add(20,30)
