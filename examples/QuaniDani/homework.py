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
 
def students_count(students):
	return len(students)

def was_present(students,name):
	
	for value in students.values():
		if value[1] == name:
			return True
	return False

def unique_was_present(students,unique_id):
	if unique_id in students.keys():
		return True
	return False

def get_all_by_name(students,name):
	dic= {}
	for value in students:
		if value[0] == name:
			dic.key = value[0]
	return (stu_sub)
	
	
def how_many_use(students,os_name):
	i=0
	for value in students.values():	
		if os_name in value[2]:
			i=i+1
	return i


def get_all_names(students):
	a = []
	for value in students.values():
		a.append(value[0])
	return set(a)


	

 
