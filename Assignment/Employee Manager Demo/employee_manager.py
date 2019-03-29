def main_menu():
    print("::Employee Management Portal::")
    print("--------------------------------------")
    print("1. Create\n2. Display\n3. Exit")
    print("---------------------------------------")
    return int(input("Enter Choice: "))


def create():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    salary = input("Enter Salary: ")
    desg = input("Enter Designation: ")

    f1 = open("emp_data.txt", 'a')
    f1.write(name + "|" + age + "|" + salary + "|"+ desg)
    f1.write("\n")
    f1.close()



def display():
    f1 = open("emp_data.txt",'r')
    for emp in f1:
        emp_det = emp.split('|')
        #print(emp_det)
        print("\n")
        print("NAME : ",emp_det[0])
        print("AGE : ",emp_det[1])
        print("SALARY: ",emp_det[2])
        print("DESIGNATION: ",emp_det[3])
        print("....................................................")
    f1.close()

def count_emp():
    f1 = open("emp_data.txt",'r')
    lines = 0
    for i in f1:
        lines +=1
    return lines



#main
choice = 0
while(choice!=3):
    print("")
    choice = main_menu()
    print("")
    if (choice==1):
        create()
    elif (choice ==2):
        print("....................................................")
        display()
    elif (choice==3):
        print ("No. of Employees: ",count_emp())
    else:
        print("Invalid Choice")
        continue
    




