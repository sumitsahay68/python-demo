from threading import *
from time import *
class A(Thread):
    def run(self):
        for i in range(1,21):
            print("i: ",i)
            sleep(0.05)

class B(Thread):
    def run(self):
        for j in range(1,21):
            print("j: ",j)

class C(Thread):
    def run(self):
        for k in range(1,21):
            print("k: ",k)
            sleep(0.5)

a1=A()
b1=B()
c1=C()


a1.start()
b1.start()
c1.start()
b1.join()

print("Program Exiting Soon.......")
