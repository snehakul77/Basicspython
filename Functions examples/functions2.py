#WAP to read and write contents from file using functions


#Function to read data from specific file and return the variable

def read_file(filepath):
    f =open(filepath,'r')
    data = f.read()
    f.close()
    return data


#process

def join_withdelim(text, delim):
    words = text.split()
    text_formatted = delim.join(words)
    return text_formatted

#write formatted data in another file

def writedata(filepath,data):
    f = open(filepath,'w')
    f.write(data)
    f.close()


#calling functions

path = "/Users/apple/Documents/sample.txt"
c = read_file(path)
#print(c)
formattedwords = join_withdelim(c,"^")
print(formattedwords)
writedata('output1.txt',formattedwords)


    
    
    
