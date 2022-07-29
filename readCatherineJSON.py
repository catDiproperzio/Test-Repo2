import json
from unicodedata import name
f=open('stack.json')
data=json.load(f)

for stuff in data['items']:
    print(stuff['owner']['display_name'])

# for i in data['people']:
#     print(i)

# print("---------------------------------------------------------------")
# f=open('catherine2.json', "r")
# data=json.loads(f.read())
# print(type(data))
# print(data)

f.close()
