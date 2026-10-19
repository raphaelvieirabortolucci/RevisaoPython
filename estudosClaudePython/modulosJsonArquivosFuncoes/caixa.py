import json


try: 

    with open("produtos.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)

except FileNotFoundError:
    produtos = [
        {
            
        }
    ]