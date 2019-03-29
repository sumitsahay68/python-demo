from customexceptiondemo import *

a=5
try:
        b  = int(input("Enter b: "))
        c = int(input("Enter c: "))     #to know Error/Exception name ..put the statement to be checked outside try
        print("sum: ",b+c)
        for i in range(10):
            print(i)
            #res = a /(a-i)
            if(i==8):
                raise AbcError
            #if(i==2):
                #raise BaseException
except ValueError as v:
    print("Please enter number only: ",v)
except ZeroDivisionError:
    print("Denominator can't be zero")
except AbcError as e:
    e.display()
except Exception as e:
    print("Default Exception Handler:  ",e)
else:
    print("Everything is fine!!")
finally:
    print("always executed")

    
print("Program continues.....")


print("======================")
