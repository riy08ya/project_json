import json

with open('data.json','r')as file:
    data=json.load(file)

data['tahun_terbit']=2005

with open('data.json','w') as file:
    json.dump(data,file,indent=4)