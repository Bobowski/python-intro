from collections import Counter
import operator


def most_used(words, n):
    with open(words, 'r') as myfile:
        data = myfile.read().replace('\n', ' ')
    words = data.split()
    dict = Counter(words)
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

    i = 0
    while n > 0:
        print(str(sorted_dict[i][1]) + " " + str(sorted_dict[i][0]))
        i += 1
        n -= 1


most_used("text.txt", 5)
