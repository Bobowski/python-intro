class AlreadyInClassException(Exception):
    pass


class Classroom(dict):
    def __init__(self, max):
        super().__init__()
        self.max_number = max

    def __setitem__(self, key, value):
        if len(self) > self.max_number or key in self.keys():
            raise AlreadyInClassException
        super().__setitem__(key, value)

    def __delitem__(self, key):
        if key in self.keys():
            super().__delitem__(key)


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
a[s1.id] = s1
a[s2.id] = s2
del a[s1.id]
print(a)
