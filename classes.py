class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("\nName: ",self.name)
        print("Age: ",self.age)



class Student:
    def __init__(self,rollno,name,age):
        self.rollno = rollno
        self.name = name
        self.age =  age

    def display(self):
        print("\nRoll No: ",self.rollno)
        print("Name: ",self.name)
        print("Age: ",self.age)


class Employee:
    def __init__(self,eid,name,age,salary,desg):
        self.eid = eid
        self.name = name
        self.age =  age
        self.salary = salary
        self.desg = desg
        
    def display(self):
        print("\nEmployee ID: ",self.eid)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        print("Designation: ",self.desg)
