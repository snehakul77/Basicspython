#WAP to create a list with elements which are common from 2 different lists.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])

print(c)


