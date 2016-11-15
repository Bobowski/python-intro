# Example solutions to Frequency Counter exercises
# Many thanks to Krzysiek Strzelecki for his solutions
# I would split it into multiple lines to make it more readable
# But it works fine :D

from collections import Counter
import re


def most_used(file, count, delimeter = " "):
    return Counter(re.split("["+delimeter+"]+",open(file).read())).most_common(count)


print(most_used("test.txt", 10))


# Below is solution based on dictionaries (simpler implementation)
def most_used2(file, count):
    words = open(file, "r").read()
    words = words.split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    l = list(freq.items())
    l = sorted(l, key=lambda x: x[1], reverse=True)
    return l[:count]

print(most_used2("test.txt", 10))
