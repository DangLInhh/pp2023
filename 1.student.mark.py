print("Input number of students in a class:")
x = int(input())
a = []
b = []
c = []
for i in range(x):
         a.append(input("Student " + str(i) + "ID: "))
         b.append(input("Student " + str(i) + "name: "))
         c.append(input("Student " + str(i) + "DOB: "))

print("Input number of courses in a class:")
y = int(input())
t = []
z = []
for w in range(y):
    t.append(input("Input course " + str(i) + "ID: "))
    z.append(input("Input course " + str(i) + "name: "))

print("Select the course you want to input mark:")
e = input()
r = []
if e in z:
  for i in range(x):
    r.append(input("Input mark for student"+str(i)+':'))
else:
    print("Please select the course again.")

for i in range(x):
    print('\n'"Student",i+1,"ID:",a[i])
    print("Student",i+1,"name:",b[i])
    print("Student",i+1,"DOB:",c[i])
for w in range(y):
    print('\n'"Course",w+1,"ID:",t[w])
    print("Course",w+1,"name",z[w])

print('\n'"STUDENT'S MARK IN COURSE",z[w],':')
for i in range(x):
    print("Student",i+1,"mark:",r[i])