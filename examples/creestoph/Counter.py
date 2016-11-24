from collections import Counter
import re
import os.path


def most_used(file, count, delimeter=" "):
    if not os.path.isfile(file) or isinstance(count, int) or count < 0 or not isinstance(delimeter, str):
        return -1
    return Counter(re.split("[" + delimeter + "]+", open(file).read())).most_common(count)


print(most_used("test.txt", 10))
