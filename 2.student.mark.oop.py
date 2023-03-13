class studentInformation:
 def __init__(Infor, name, ID, DOB):
    Infor.name = name
    Infor.ID = ID
    Infor.DOB = DOB
 def myfunc(Infor):
     print("Student ",i+1,"name:" ,Infor.name)
     print("Student ",i+1,"ID:" , Infor.ID )
     print("Student ",i+1,"DOB:" , Infor.DOB) 
print("Input number of students:")
x = int(input())
student = []
for i in range(x):
    StudentID = input("Student " + str(i+1) + " ID: ")
    StudentDOB = input("Student " + str(i+1) + " name: ")
    StudentName = input("Student " + str(i+1) + " DOB: ")
    students = studentInformation(StudentName, StudentID, StudentDOB)
    student.append(students)

class courseInformation:  
    def __init__(course, name, ID):
     course.ID = ID
     course.name = name  
    def myfunc2(course):
     print("Course ",w+1,"name:", course.name)
     print("Course ",w+1,"ID:", course.ID ) 
print("Input number of courses in a class:")
y = int(input())
courses = []
couID = []
for w in range(y):
    couID.append(w)
    print("Input ID of course",w+1)
    couID[w] = input()
    print("Input name of course",w+1)
    couname = input()
    course = courseInformation(couID[w], couname)
    courses.append(course)

class markInformation:
   def __init__(mark, grade):
      mark.grade = grade
   def myfunc3(mark):
      print("Student's",i+1,"score:", mark.grade)
print("The course's ID you want to input mark:")
intput = input()
Mark = []
if intput in couID:
 for i in range(x):
   print("Mark for student",i+1,":")
   Score = int(input())
   Marklists = markInformation(Score)
   Mark.append(Marklists)
else:
 print("Invalid ID.")
print('\n')
for i in range(x):
    print('\n')
    student[i].myfunc()
for w in range(y):
   print('\n')
   courses[w].myfunc2()
print("\n")
for i in range(x):
   Mark[i].myfunc3()
