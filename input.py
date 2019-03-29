a= int(input("Enter a:"))
b= int(input("Enter b:"))
c= a+b;
print("Result: ",c)

#reading one character
confirm = input("Do you want to continue?: ")[0] #[0:4] etc.. like substring
if confirm=="y":
    print("You chose to continue...");     #block,suites
else:
    print("You chose to exit.")

print (confirm)
