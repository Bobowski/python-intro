class AlreadyInClassException(Exception):
    pass


class Classroom(dict):
    def __init__(self, max):
        super().__init__()
        self.max_number = max

    def add_student(self, student):
        if len(self) > self.max_number or self.has_student(student.id):
            raise AlreadyInClassException
        self[student.id] = student

    def remove_student(self, student):
        if self.has_student(student.id):
            del self[student.id]

    def has_student(self, id):
        return id in self.keys()


class Student:
    def __init__(self, id, first_name, last_name, courses):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.courses = list(courses)

    def __str__(self):
        return str(self.id) + ' ' + self.first_name + ' ' + self.last_name + ' ' + str(self.courses)

    def __repr__(self):
        return '(' + self.first_name + ' ' + self.last_name + ' ' + str(self.courses) + ')'


a = Classroom(10)
s1 = Student(1, "Krzysiek", "Strzelecki", ("Informatyka",))
s2 = Student(2, "Adam", "Bobowski", ("Informatyka", "Costam"))
a.add_student(s1)
a.add_student(s2)
print(a)
