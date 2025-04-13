#WAP read the data from the file and write the text in another file and add hypen in between words

path = "/Users/apple/Documents/sample.txt"

f = open(path,'r')
data = f.read()
f.close()

#Process

words = data.split()
text_formatted = "-".join(words)
print(text_formatted)

#Writing hypen added words in another file

f = open('output.txt','w')
f.write(text_formatted)
f.close()
