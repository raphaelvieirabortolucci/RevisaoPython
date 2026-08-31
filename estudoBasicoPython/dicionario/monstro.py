import random

tipos_monstros = ['esqueleto', 'fada', 'espito sombrio', 'diabretes',
                  'gigante']
locais_encontro = ['floresta negra', 'outro dimenção', 'cemiterio']

tipo = random.choice(tipos_monstros)
local = random.choice(locais_encontro)

monstro_dict = {
    "Vida": random.randint(10, 50),
    "Ataque": random.randint(1, 8),
}
print(f"Tipo:{tipo}")
print(f"Local:{local}")
print(f"Vida:{monstro_dict['Vida']}")
print(f"Ataque: {monstro_dict['Ataque']}")