friends = {"Antek": 1, "Bolek": 2, "Czesio": 3, "Daniel": 2, "Emil": 5, "Adam": 2}
friend_names = [a for a in friends]


def x(a, tab):
    if a not in tab:
        tab.append(a)
        return True
    return False


tab = []
special_trades = [a for a in friends.values() if x(a, tab)]

friends_names_new = {k: [friends[k]] for k in friends}

friends_names_new = {k: [friends[k]] for k in friends}
friends_names_new = {k: friends_names_new[k] if k[0] != 'A' else friends_names_new[k]+["awesome"] for k in friends}
friends_inverted = {friends[k]:k for k in friends}

print(friends_inverted)


a = ["Awesome", "Awesomeness"]
b = [list(a) for _ in range(3)]
b.append(["Awesome", "Awesomeness"])
a.append("End")
print(b)
