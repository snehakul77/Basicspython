names = ["Alice", "Bob", "Christina", "Dan", "Eve"]

sorted_names = sorted(names, key=lambda name: len(name))

for name in sorted_names:
    print(name)