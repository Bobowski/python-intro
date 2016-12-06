students_list = {
    0: ("Adam", 7, ["Linux", "Windows", "Mac OS"]),
    1: ("Konrad", 3, ["Linux"]),
    2: ("Monika", 3, ["Linux", "Windows"])
}


def students_count(student_list):
    return len(student_list)


def was_present(student_list, name):
    return name in [value[0] for value in student_list.values()]


def get_all_by_name(student_list, name):
    return {key: value for key, value in student_list.items() if value[0] == name}

