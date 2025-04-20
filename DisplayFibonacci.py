#WAP to display fibonacci sequence using recursion

def recur_fibonacci(num):
    if num <= 1:
        return num
    else:
        return(recur_fibonacci(num-1) + recur_fibonacci(num-2))

nterms = int(input("Enter the number of terms: "))

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(recur_fibonacci(i))
