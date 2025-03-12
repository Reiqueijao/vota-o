import json

with open("Data\Palavras.json","r") as f:
    data = json.load(f)
print(data["messages"][0]['author']["id"])
