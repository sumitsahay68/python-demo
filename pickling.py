import pickle
from person import Person

p1 = Person("Sumit",21)

f1  = open("person.ser",'wb')
pickle.dump(p1,f1)
f1.close()
print("Pickled succesfully.....")
