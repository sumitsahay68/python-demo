class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        print("NAME : ", self.name)
        print("AGE : ",self.age)
        return ""


