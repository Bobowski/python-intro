def students_count(students):
    return len(students)


def was_present(students, name):
    return name in [a[0] for a in students.values()]


def unique_was_present(students, unique_id):
    return unique_id in students.keys()


def get_all_by_name(students, name):
    return {k: students[k] for k in students if students[k][0] == name}


def get_all_by_semester_range(students, sem_from, sem_to):
    return {k: students[k] for k in students if sem_from >= students[k][1] <= sem_to}


def how_many_use(students, os_name):
    return len({k: students[k] for k in students if os_name in students[k][2]})


def get_all_names(students):
    return [students[k][0] for k in students]

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

print(students_count(students))
print(was_present(students, "Piotrek"))
print(get_all_by_name(students, "Krzysiek"))
print(get_all_by_semester_range(students,1,3));
print(how_many_use(students, "Linux"))
print(get_all_names(students))
