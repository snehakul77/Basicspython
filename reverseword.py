#WAP that asks user for a long string containing multiple words and print back user with a string except the words are displayed in backwords order.

sample = input("Enter a string: ")
sample = sample.split()
print(sample)

reversed = " ".join(sample[::-1])
print(reversed)