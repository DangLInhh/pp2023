import numpy as np
import math
import curses
class studentInformation:
 def __init__(Infor, name, ID, DOB):
    Infor.name = name.decode('utf-8')
    Infor.ID = ID.decode('utf-8')
    Infor.DOB = DOB.decode('utf-8')
 def myfunc(Infor):
     return(f"Student name: {Infor.name}\nStudent ID: {Infor.ID}\nStudent's Dob:{Infor.DOB}" )

class courseInformation:  
    def __init__(courses, name, ID, credit):
     courses.ID = ID.decode('utf-8')
     courses.name = name.decode('utf-8')
     courses.credit = credit
    def myfunc2(course):
     return(f"Course name: {course.name}\nCourse ID: {course.ID}\nCourse credit:{course.credit}")

class markInformation:
   def __init__(mark, grade, cou):
      mark.grade = grade
      mark.cou = cou
   def myfunc3(mark):
      return(f"Student's score: {math.floor(mark.grade)}")

def main(stdscr):
   stdscr.clear()
   curses.echo()
   stdscr.addstr("Input number of students:")
   x = int(stdscr.getstr())
   student = []
   for i in range(x):
      stdscr.clear()
      stdscr.addstr("Student " + str(i+1) + " ID: ")
      StudentID = stdscr.getstr()
      stdscr.clear()
      stdscr.addstr("Student " + str(i+1) + " name: ")
      StudentName = stdscr.getstr()
      stdscr.clear()
      stdscr.addstr("Student " + str(i+1) + " DOB: ")
      StudentDOB = stdscr.getstr()
      students = studentInformation(StudentName, StudentID, StudentDOB)
      student.append(students)

   stdscr.addstr("Input number of courses in a class:")
   y = int(stdscr.getstr())
   Courselist = []
   couID = []
   for w in range(y):
      couID.append(w)
      stdscr.clear()
      stdscr.addstr("Input ID of course"+ str(w+1)+ ":")
      couID[w] = stdscr.getstr()
      stdscr.clear()
      stdscr.addstr("Input name of course" + str(w+1)+ ":")
      couname = stdscr.getstr()
      stdscr.clear()
      stdscr.addstr("Input credit of course" +str(w+1)+ ":")
      coucre = float(stdscr.getstr())
      course = courseInformation(couID[w], couname, coucre)
      Courselist.append(course)

   Mark = [[0 for i in range(x)] for w in range(y)]
   for w in range(y):
     stdscr.clear()
     stdscr.addstr(f"Student marks in course{w+1}: ")
     for i in range(x):
      stdscr.addstr(f"\nMark for student {i+1}:")
      Score = float(stdscr.getstr())
      Mark[w][i] = Score
   Markarray = np.asarray(Mark)

   stdscr.clear()
   for i in range(x):
      stdscr.addstr('\n')
      stdscr.addstr(f'{student[i].myfunc()} ')
      stdscr.addstr('\n')
   for w in range(y):
      stdscr.addstr('\n')
      stdscr.addstr(f'{Courselist[w].myfunc2()}')
      stdscr.addstr('\n')
   stdscr.addstr('\n')
   for w in range(y):
    for i in range(x):
      stdscr.addstr('\n')
      stdscr.addstr(f"Student {i+1} mark: {Markarray[w][i]} in course {w+1}")

   coucre = [cou.credit for cou in Courselist]
   coursecreditarr = np.array(coucre)
   markarr = np.array(Mark)
   gpa = np.dot(markarr.T, coursecreditarr) / np.sum(coursecreditarr)
   sortedgpa = np.argsort(gpa)[::-1]
   stdscr.addstr(f" ")
   for i in sortedgpa:
      stdscr.addstr('\n')
      stdscr.addstr(f"\nStudent's {i+1} GPA in order descending: {gpa[i]}")    
      stdscr.getkey()

curses.wrapper(main)