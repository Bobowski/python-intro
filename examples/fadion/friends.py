friends = {"nie": 1, "mam": 2, "przyjaciol": 3, "to": 1, "straszne": 3, "A": 5, "a": 6}

friend_names = list(friends.keys())

special_trades = list(friends.values())
special_trades.sort()
set2 = set()
for i in range(0, len(special_trades)):
    set2.add(special_trades[i])
special_trades = list(set2)

friends2 = {"nie": [1], "mam": [2], "przyjaciol": [3], "to": [1], "straszne": [3], "A": [5], "a": [6]}

f2_names = list(friends2.keys())
for i in range(0, len(f2_names)):
    if f2_names[i][0] == "a" or f2_names[i][0] == "A":
        friends2[f2_names[i]].append("Awesome")

print(friend_names)
print(special_trades)
print(friends2)
