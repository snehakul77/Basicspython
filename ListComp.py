#WAP in one line where there a list and create another list that has only even elements of 1st list

a = [1,2,3,4,5,6,7,8,9]
b = []

b = [i for i in a if i % 2 == 0]
print(b)

