from menus import *
from employeeclasses import *
from numpy import *

def main():
    #employees = array([],Employee)
    employees = []
    ch1 = main_menu()
    while(ch1!=4):
        if(ch1 == 1):
            ch2 = create_menu()
            while(ch2!=4):
                if(ch2<4 and ch2>0):
                    data = store()
                if(ch2==1):
                   employees.extend([Clerk(data[0],data[1])])
                elif(ch2==2):
                   employees.extend([Programmer(data[0],data[1])])
                elif(ch2==3):
                    employees.extend([Manager(data[0],data[1])])
                else:
                    print("Invalid Choice\n")
                    ch2 = create_menu()
                    continue
                ch2 = create_menu()

        elif(ch1 == 2):
            #Employee.display()
            for emp in employees:
                print("\nNAME: ",emp.name)
                print("AGE: ",emp.age)
                print("SALARY: ",emp.salary)
                print("DESIGNATION: ",emp.desg)

        elif(ch1 == 3):
            #emp = Emps()
            for employee in employees:
                Emps.incr(employee)
            
        else:
            print("Invalid Input\n")

        ch1 = main_menu()
                               
    print("No. of Employees Created : ",Employee.count)
