#WAP to check if a number is armstrong number

num = int(input("ENter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += pow(digit, 3)
    temp = temp // 10

if num == sum:
    print(num, "is a Armstrong number")
else:
    print(num, "is not a Armstrong number")

