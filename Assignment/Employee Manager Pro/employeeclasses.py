class Employee:
    count = 0
    def __init__(self,name,age,salary,desg):
        #self.empid = empid
        self.name = name
        self.age = age
        self.salary = salary
        self.desg = desg
        #fwrite = open("emp_data.txt",'a')
        #fwrite.write("\n"+self.name+"|"+str(self.age)+"|"+str(self.salary)+"|"+self.desg)
        #fwrite.close()
        
        Employee.count+=1

    
    @staticmethod
    def display():
        pass
        #fread =  open("emp_data.txt",'r')
        #for emp in fread:
            #data = emp.split("|")
            #print("\nNAME: ",data[0])
            #print("AGE: ",data[1])
            #print("SALARY: ",data[2])
            #print("DESIGNATION: ",data[3])
        #fread.close()

        
class Clerk(Employee):
    def __init__(self,name,age):
        super().__init__(name,age,8000,"Clerk")
        
    def raiseSalary(self):
        self.salary+=2000
        

class Manager(Employee):
    def __init__(self,name,age):
        super().__init__(name,age,80000,"Manager")
    def raiseSalary(self):
        self.salary+=10000

class Programmer(Employee):
    def __init__(self,name,age):
        super().__init__(name,age,25000,"Programmer")
    def raiseSalary(self):
        self.salary+=5000

class Emps:
    def incr(self,obj):
        obj.raiseSalary()
    
    
