#WAP to check if a number is prime number or not

num = int(input("Enter a number: "))

flag = False

if num == 0 and num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")