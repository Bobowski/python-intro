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


def students_count(dictionary):
    return len(dictionary)


def was_present(dictionary, name):
    return name in [value[0] for value in dictionary.values()]


def unique_was_present(dictionary, unique_id):
    return unique_id in dictionary.keys()


def get_all_by_name(dictionary, name):
    return {key: value for key, value in dictionary.items() if value[0] == name}


def get_all_by_semester_range(dictionary, sem_from, sem_to):
    return {key: value for key, value in dictionary.items() if sem_from <= value[1] <= sem_to}


def how_many_use(dictionary, os_name):
    return len({key: value for key, value in dictionary.items() if (os_name in value[2])})


def get_all_names(dictionary):
    return set([value[0] for value in dictionary.values()])


print(students_count(students))
print(unique_was_present(students, 11))
print(was_present(students, "Kuba"))
print(get_all_by_name(students, "Krzysiek"))
print(get_all_by_semester_range(students, 4, 7))
print((how_many_use(students, "Linux")))
print(get_all_names(students))
