import json
f=open('catherine.json')
data=json.load(f)

for i in data['catherine']:
    print(i)
print("---------------------------------------------------------------")
f=open('catherine2.json', "r")
data=json.loads(f.read())
print(type(data))
print(data)

f.close()
