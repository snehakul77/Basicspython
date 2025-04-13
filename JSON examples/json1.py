#Read the Json_data file and print ID

import json

f = open("Json_data.txt",'r')
json_data = f.read()
f.close()

json_data = json.loads(json_data)

print(json_data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossTerm"])
