class Classroom:
	def __init__(self,count):
		self.count = count
		self.students = {}
	
	
	def add_student(self,student):
		if len(self.students) < self.count:
			if student.uid in self.students.keys():
				raise AlreadyInClassroomException
			self.students[student.uid] = student
	
	def remove_student(self,student):
		del self.students[student.uid]
	
	def has_student(self,student):
		if student.uid in self.students.keys():
			return True
		return False

class Student:
	def __init__(self,uid,name,lname,courses):
		self.uid = uid
		self.name = name
		self.lname = lname
		self.courses = courses


class AlreadyInClassroomException:
    pass
    
a = Classroom(5)

A = Student(1,"a","b","c")
B = Student(2,"d","e","f")
a.add_student(A)
print (a.has_student(A))
a.add_student(B)

