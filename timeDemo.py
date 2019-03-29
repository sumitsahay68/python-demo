import time

ms =  time.time()
print ("Milliseconds : ",ms);
print("Current time: ", time.localtime(ms))
print("Meaningful Time: ",time.asctime(time.localtime(ms)))
if(str(time.asctime(time.localtime(ms))) == "Mon Mar 25 18:00:00 2019"):
    print("Time to go...")
print("-----------------------------------")

import calendar

cal = calendar.month(2019,4,10,2)
print(cal)

print("-----------------------")
str="hEWLKOooo  eVEeryBodyYY"

print(str.center(30,"$"))
