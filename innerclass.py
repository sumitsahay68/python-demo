class Emp:
    def __init__(self,name,age,state,city,pin):
        self.name = name
        self.age = age
        self.addr = Address(state,city,pin)
        self.computer = self.Computer("HP","AB-210TX","Intel Core i7 6550","3.1GHz","8GB")

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        self.addr.display()
        self.computer.display()
        
    class Computer:
        def __init__(self,brand,model,processor,speed,ram):
            self.brand = brand
            self.model = model
            self.processor = processor
            self.speed = speed
            self.ram = ram
        def display(self):
            print("Company: ",self.brand)
            print("Model: ",self.model)
            print("Processor: ",self.processor)
            print("Clock Speed: ",self.speed)
            print("RAM: ",self.ram)
    
    

class Address:
    def __init__(self,state,city,pin):
        self.state =  state
        self.city = city
        self.pin = pin
    def display(self):
        print("State : ",self.state)
        print("City: ",self.city)
        print("PIN: ",self.pin)


e1 = Emp("Sumit",21,"Karnataka","Bangalore",560045)
e1.display()

e1.computer = Emp.Computer("Dell","Alienware","Core i9","3.1GHz","16GB")
e1.display()

print("===================================")
print("===================================")
print("===================================")

c1 = Emp.Computer("Dell","Alienware","Core i9","3.1GHz","16GB")
c2 = Emp.Computer("Dell","Alienware","Core i9","3.1GHz","16GB")

c1.display()
print()
c2.display()
print();
print(id(c1))
print(id(c2))
