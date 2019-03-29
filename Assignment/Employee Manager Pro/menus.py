from exceptions import *

def main_menu():
        print("----------------------")
        print("1. Create\n2. Display\n3. Raise Salary\n4. Exit")
        print("----------------------")
        try:
                choice = int(input("Enter Choice: "))
                print()
                return choice
        except ValueError as e:
                print("Choice must be numeric only " ,e)

def create_menu():
        print("----------------------")
        print("1. Clerk\n2. Programmer\n3. Manager\n4. Main Menu")
        print("----------------------")
        try:
            choice = int(input("Enter Choice: "))
            print()
            return choice
        except ValueError as e:
                print("Choice must be numeric only " ,e)

def store():
    print("----------------------")
    try:
        name = input("Enter Name: ")
        if(not name.isalpha()):
            raise EmpNameError
        age  = AgeError.readAge()
        return [name,age]
    except EmpNameError as e:
        e.display()
    except AgeError as e:
        e.display()
    except ValueError as e:
        print("Age must be numeric only: ",e)
