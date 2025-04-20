#WAP to takes a list and returns a new list that contains all the first elements of the list removing all the duplicates.


def duplicates(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

a = [1,1,3,5,2, 3, 4]
print(a)
print(duplicates(a))