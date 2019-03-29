f1=open("abc.txt", "r") 

print(f1.readline(), end = "");
print(f1.readline(), end = "");
print(f1.readline(), end = "");
print(f1.readline(), end = "");
print(f1.readline(), end = "");
#f1.seek(699)
print(f1.readline(), end = "");
#f1.close();


f2=open("xyz.txt",'a')
f2.write("hejkjkdfjkal")
f2.close()

#reading binary files

f3 = open("icon.png", 'rb')
#print(f3.read())

f4 = open("copy.txt",'wb')
for data in f3:
    f4.write(data)
f4.close()
