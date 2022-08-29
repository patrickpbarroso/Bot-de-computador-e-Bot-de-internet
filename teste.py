import json

with open("frases.json") as meu_json:
    frases = json.load(meu_json)

print(frases[1]["phrase"])