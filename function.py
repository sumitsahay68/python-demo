def abc(a,b):   #required type
    print("a : ",a)
    print("b : ",b)


def xyz(a,b):   #any order type / keyword argument type
    print("a : ",a)
    print("b : ",b)

def  pqr(a,b,c=40,d=60):   #default arg type
    print("a : ",a)
    print("b : ",b)
    print("c : ",c)
    print("d : ",d)


def klm(*a):      # 0 or more ..if (a,*b)  1 or more & so on...           #var-arg type
    res=0
    for i in a:
        res = res + int(i)
    print(res)

abc(10,20)
#abc(10,20,30)
print("---------")
xyz(20,30)
print()
xyz(b=20,a=30)
print("---------")
pqr(20,40,23)
print()
pqr(20,35)
print("---------")
klm(50,40)
print()
klm(20,40,99)
print()
klm(32)
print()
klm()
