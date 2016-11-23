def most_used(text, x):
    words = open(text, 'r').read()
    words = words.split()

    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    l = list(dic.items())
    l = sorted(l, key=lambda i: i[1], reverse=True)
    return l[:x]


print(most_used("t.txt", 100))
