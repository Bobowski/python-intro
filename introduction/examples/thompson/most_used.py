from collections import Counter
import operator


def most_used(words, n):
    with open(words, 'r') as myfile:
        data = myfile.read()
        data = data.replace('\n', ' ')
    words = data.split()
    dicti = Counter(words)
    sorted_dict = sorted(dicti.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(0, n):
        print(str(sorted_dict[i][1]) + " " + str(sorted_dict[i][0]))


most_used("text.txt", 1)
