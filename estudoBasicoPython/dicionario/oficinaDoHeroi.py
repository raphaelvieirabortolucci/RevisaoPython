import random

racas = ["humano", "elfo", "elfo", "meio-org", "gnomo"]
classe = ['guerreiro(a)', 'mago(a)', 'ladino(a)', 'clerigo', "barbaro(a)"]

nome_inicio = ['carlos', 'natasha', 'mario', 'fernada', 'joao']
nome_final = ['silva', 'lopes', 'vieira', 'bennis', 'rocha']

print("--- BEM VINDO A FORJA DE HEROIS ---")
print("estamos criando um novo aventureiro ...")
raca_heroi = random.choice(racas)
classe_heroi = random.choice(classe)
nome_heroi = "{random.choice(nome_inicio)} {random.choice(nome_final)}"

print('Mochila do heroi')
itens_iniciais = ["Pocao de Cura", "Adaga Enferrujada", "Escudo de Madeira",
                  "Maca", "Mapa Antigo"]

loot = ["pocao de cura", "adaga enferrujada", "escudo de madeira", "maca",
        "mapa antigo"]
mochila_heroi = []
for i in range(3):
    mochila_heroi.append(random.choice(loot))

ficha_final = {
    "nome": nome_heroi,
    "raca": raca_heroi,
    "classe": classe_heroi,
    "forca": random.randint(3, 18),
    "inteligencia": random.randint(3, 18),
    "destreza": random.randint(3, 18),
    "carisma": random.randint(3, 18),
    "itens": mochila_heroi
}

print('\n--- ficha pronta ---')
print(f"nome: {ficha_final['nome']}")
print(f"itens: {ficha_final['itens']}")
print(f"raca: {ficha_final['raca']}")
print(f"clase: {ficha_final['classe']}")
print(f"forca: {ficha_final['forca']}")
print(f"inteligencia: {ficha_final['inteligencia']}")
print(f"destreza: {ficha_final['destreza']}")
print(f"carisma: {ficha_final['carisma']}")
