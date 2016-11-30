class Classroom(object):
    def __init__(self, count):
        self.count = count
        self.students = {}

    def add_student(self, student):
        if len(self.students) < self.count:
            if student.uid in self.students.keys():
                raise AlreadyInClassroomException
            self.students[student.uid] = student

    def remove_student(self, student):
        del self.students[student.uid]

    def has_student(self, student):
        if student.uid in self.students.keys():
            return True
        return False


class Student(object):
    def __init__(self, uid, name, lname, courses):
        self.uid = uid
        self.name = name
        self.lname = lname
        self.courses = courses


class AlreadyInClassroomException(Exception):
    pass


a = Student(0, "A", "B", ["Python"])
c = Student(1, "C", "D", ["Python"])
b = Classroom(10)
b.add_student(a)
# b.add_student(a)
b.add_student(c)
print([student.uid for student in b.students.values()])
print([student.lname for student in b.students.values()])
print(b.has_student(c))
b.remove_student(c)
print([student.lname for student in b.students.values()])
print(b.has_student(c))
