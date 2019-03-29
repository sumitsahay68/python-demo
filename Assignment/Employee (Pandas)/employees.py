import pandas as pd

df  = pd.read_csv("emp_data.csv",delimiter = ",",names=['id','name','age','salary','designation','dept','project_id','project_name','manager','city','state'])

print("=======Eldest Employees===========")
maxage = df.max()['age']
print(df[df.age==maxage])
print()
print("=======Youngest Employees===========")
minage = df.min()['age']
print(df[df.age == minage])

print()
print("=======2nd Highest Paid Employees===========")
maxsal = df.max()['salary']
df2=df[df.salary!=maxsal]
secmax = df2.max()['salary']
print(df[df.salary == secmax])
print()

print("=======Cost Dept Wise===========")  #'Development'|'Testing'|'Management
deptgroup = df.groupby('dept')

for name,group in deptgroup:
    print("::DEPT: ",name)
    print(group)
    print("\nDepartment Cost: Rs.",group.sum()['salary'])
    mean_age = group.mean()['age']
    if(mean_age<35):
        print("YOUNGSTER'S DEPARTMENT: ",int(mean_age))
    else:
        print("ELDER'S DEPARTMENT: ",int(mean_age))
    print("--------------------------------------------------------------------------------------------------------------------------------")


print()

print("=======Cost Project Wise===========")  
projgroup = df.groupby('project_name')

for name,group in projgroup:
    print("::PROJECT: ",name)
    print(group)
    print("\nProject Cost: Rs.",group.sum()['salary'])
    print("--------------------------------------------------------------------------------------------------------------------------------")

print()
print("=======Manager Wise Employees===========")  #Harvey Reeves|Emily Beck|Adam McDaniel|Lily Elliott|Charles Perez
mgrgroup = df.groupby('manager')

for name,group in mgrgroup:
    print("::MANAGER: ",name)
    print(group)
    print("--------------------------------------------------------------------------------------------------------------------------------")

    
print()

print("=======Search by ID===========")
eid = int(input("Enter Employee ID: "))
print(df[df.id == eid])


print()
print("======================FILLNA DEMO=============================================")
dfn =pd.read_csv("emp_data2.csv",delimiter = ",",names=['id','name','age','salary','designation','dept','project_id','project_name','manager','city','state'])
dfn['designation'].fillna("Employee",inplace =True)
print(dfn)
