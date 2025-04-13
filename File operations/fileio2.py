#WAP read the text from file line by line and print line which has "the" in the line.

path = "/Users/apple/Documents/sample.txt"
f = open(path,'r')
data = f.readlines()
f.close()
#print(data)

for line in data:
    if "the" in line:
        print(line)
