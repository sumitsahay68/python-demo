y=1

def abc():
    x=1
    print("x : ",x)
    x+=1

def xyz():
    global y
    print("y : ",y)
    y+=1;

abc()
abc()
abc()
abc()
abc()
print("----------------------")
xyz()
xyz()
xyz()
xyz()
xyz()


