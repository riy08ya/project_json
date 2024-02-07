import json

data = {
    "judul" : "Aku",
    "pengarang" : "Andi M.Ahmad",
    "tahun_terbit" : 2000,
    "kota" : "malang"
}

with open ('data.json','w') as file:
    json.dump(data, file, indent=4)