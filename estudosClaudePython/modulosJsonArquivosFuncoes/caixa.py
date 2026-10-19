import json
from funcoes import carregarProd

listaCompras = []
valor = 0
while True:
    print("BEM VINDO A PAPELARIA" \
    "O que você deseja comprar (digite fim para sair)")
    carregarProd()
    for produto in carregarProd():
        print(f"Nome: {produto["nome"]}")
        print(f"Preco: {produto["preco"]}")
        print(f"Estoque: {produto["estoque"]}")
    break