class A :
    z = 30
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def display(self):
        print("x : ",self.x)
        print("y : ",self.y)

    @classmethod
    def abc(cls):
        print("From Class Method : ",cls.z)

    @staticmethod
    def xyz():   #static method
        print("This is from static method....")
        


a1 = A(10,20)
a1.display()
A.abc()
A.xyz()
