class AgeError:
    def readAge():
        while(True):
            try:
                    age = int(input("Enter Age: "))
                    if(age<21 or age>60):
                        print("Age must be between 21 and 60")
                        continue
                    return age
            except ValueError as e:
                print("Age must be numeric : ",e)
                
                
        
class EmpNameError(Exception):
    def display(self):
        print("Name must contain only alphabetic character")
