class Student:
    def __init__(self, id, fname, lname, courses):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.courses = courses


class Classroom:
    def __init__(self, capacity):
        self.capacity = capacity
        self.students = []

    def add_student(self, student_id):
        if not isinstance(student_id, int) or len(self.students) >= self.capacity or student_id in self.students:
            return False
        else:
            self.students.append(student_id)
            return True

    def remove_student(self, student_id):
        if student in self.students:
            self.students.remove(student_id)
            return True
        else:
            return False

    def has_student(self, student_id):
        return student_id in self.students


classroom = Classroom(2)

student = Student(1, "Zenek", "Rogacz", ["Python", "C++"])
student2 = Student(2, "Stefan", "Bąk", ["C#", "JS"])
student3 = Student(3, "Adam", "Kowalski", ["Java", "C++"])
student3 = Student(4, "Marzena", "Wróbel", ["Java", "C++"])

classroom.add_student(1)
classroom.add_student(2)
classroom.add_student(3)
classroom.add_student(3)
