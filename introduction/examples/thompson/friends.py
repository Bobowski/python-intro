# zadanie 1
friends = {"John": "polite", "Andrew": "kind", "Suzy": "wise", "Claire": "joyful", "Brian": "kind"}

# zadanie 2
friends_names = list(friends.keys())
special_trades_list = list(set(friends.values()))

# zadanie 3
special_trades = [e for e in friends.values() if list(friends.values()).count(e) < 2]

# zadanie 4
friends_trades = {}

for person in friends:
    if person.startswith("A"):
        friends_trades.update({person: [friends[person], "awesome"]})
    else:
        friends_trades.update({person: [friends[person]]})

# list comprehension
# zadanie 2
friends_names_2 = [e for e in friends.keys()]

# zadanie 3

# zadanie 4
# friends_trades_2 = {key: value for (key, value) in friends lambda key: key if key[0] != 'A' else value }
