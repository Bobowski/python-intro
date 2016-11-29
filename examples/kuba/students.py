# Dictionary that represents students from last class.
# Key: unique id, Value: (name, semester, list of favorite OS's)
students = {
    0: ("Adam", 7, ["Linux", "Windows 10", "Mac OS"]),
    1: ("Konrad", 3, ["Linux"]),
    2: ("Monika", 3, ["Linux", "Windows"]),
    3: ("Piotrek", 3, ["Linux"]),
    4: ("Kuba", 3, ["Mac OS"]),
    5: ("Krzysiek", 3, ["Linux"]),
    6: ("Krzysiek", 3, ["Windows 10"]),
    7: ("Adam", 1, ["Windows 10"]),
    8: ("Marcel", 1, ["Windows 10"]),
    9: ("Paulina", 1, ["Windows 10"]),
    10: ("Sebastian", 1, ["Windows 10"])
}
# students_count(students) - number of students in class
print(len(students))

# was_present(students, name) returns True only if someone of given name was on last class.
def was_present(students, name):
    for klucz, abbrev in students.items():
        while abbrev[0] != name:
            return False
        return True

print(was_present(students, "Daniel"))

#for klucz, abbrev in students.items():
 #   print((klucz, abbrev))

# unique_was_present(students, unique_id) returns True only if someone of given unique_id was on last class.
def unique_was_present(students, unique_id):
    if unique_id in students:
        return True
    else:
        return False
print(unique_was_present(students, 70))

# get_all_by_name(students, name) that returns sub-dictionary of students of given name.
def get_all_by_name(students, name):
    substudents = {}
    for klucz, abbrev in students.items():
        if abbrev[0] == name:
            substudents[klucz] = abbrev
    return substudents

print(get_all_by_name(students, "Kuba"))

#Write function get_all_by_semester_range(students, sem_from, sem_to)
# that returns sub-dictionary of students that are on any semester starting from sem_from up to sem_to inclusive.

def get_all_by_semester_range(students, sem_from, sem_to):
    substudents = {}
    for klucz, abbrev in students.items():
        if abbrev[1] <= sem_to and abbrev[1] >= sem_from :
            substudents[klucz] = abbrev
    return substudents

print(get_all_by_semester_range(students, 1, 2))

#how_many_use(students, os_name) that returns how many students use os_name operating system.

def how_many_use(students, os_name):
    counter = 0
    for klucz, abbrev in students.items():
        for i in abbrev[2]:
            if i == os_name:
                counter += 1
    return counter

print(how_many_use(students, "Mac OS"))

# get_all_names(students) that returns list of all the names of students.

def get_all_names(students):
    list = []
    for klucz, abbrev in students.items():
        list.append(abbrev[0])
    return list

print(get_all_names(students))