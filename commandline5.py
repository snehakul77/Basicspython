#WAP to get output of inet and print line with has ipv4 in it

import subprocess


response = subprocess.check_output(['ifconfig'])

#print(response)

#convert byte data to string data to traverse through output

response = response .decode('utf-8')
#print(type(response))

#Traverse through the line

lines = response.split("\n")
print(lines)

for line in lines:
    if "inet" in line:
        print(line)
        break
  
        
