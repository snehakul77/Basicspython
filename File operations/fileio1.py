#WAP to count all the words from given text

f = open('/Users/apple/Documents/sample.txt','r')
data = f.read()
f.close()
#print(data)
words = data.split()
#print(words)

#Travere each and every word to get the count

d = {}
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] = d[word] + 1
print(d)
