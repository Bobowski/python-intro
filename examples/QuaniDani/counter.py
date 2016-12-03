def most_used(file):
	
	
    f = open(file, "r").read()
    f = f.split()

    dic = {}
    for i in f:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    l = list(dic.items())
    
    return l
