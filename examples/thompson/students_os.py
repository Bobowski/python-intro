students_list = {
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

def students_count(students):
    return len(students)


def was_present(students, name):
    return name in [value[0] for value in students.values()]


def unique_was_present(students, unique_id):
    return unique_id in students.keys()


def get_all_by_name(students, name):
    return {key: value for key, value in students.items() if value[0] == name}


def get_all_by_semester_range(students, sem_from, sem_to):
    return {key: value for key, value in students.items() if sem_to >= value[1] >= sem_from}


def how_many_use(students, os_name):
    return len({key: value for key, value in students.items() if (os_name in value[2])})


def get_all_names(students):
    return set([value[0] for value in students.values()])


print(students_count(students_list))
print(was_present(students_list, "Adam"))
print(unique_was_present(students_list, 11))
print(get_all_by_name(students_list, "Adam"))
print(get_all_by_semester_range(students_list, 1, 1))
print(how_many_use(students_list, "Mac OS"))
print(get_all_names(students_list))
