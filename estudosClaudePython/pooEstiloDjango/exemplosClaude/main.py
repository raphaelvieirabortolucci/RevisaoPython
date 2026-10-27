from datetime import date, timedelta

from produtos import Produto, ProdutoPerecivel, ProdutoLiquido, ProdutoCongelado

hoje = date.today()

# Lista com objetos de classes DIFERENTES (todos são "Produto", por herança)
produtos = [
    Produto("Caderno", 18.90, 40, custo=10.00),
    ProdutoPerecivel("Iogurte", 6.00, 25, custo=3.50, validade=hoje + timedelta(days=4)),
    ProdutoPerecivel("Queijo", 22.00, 10, custo=14.00, validade=hoje + timedelta(days=30)),
    ProdutoLiquido("Suco de uva", 9.50, 30, custo=5.00, volume_ml=1500, embalagem="Caixa"),
    ProdutoCongelado("Pizza", 32.00, 12, custo=20.00, temperatura_c=-18),
]

# ---------- POLIMORFISMO ----------
# O MESMO comando (print) e a MESMA chamada (calcular_preco_final) se comportam
# de um jeito diferente em cada classe, sem nenhum if para checar o tipo.
print("=== CATÁLOGO (polimorfismo) ===")
for p in produtos:
    print(p)                                   # chama __str__ -> descricao() de cada classe

print("\n=== PREÇO FINAL (polimorfismo) ===")
for p in produtos:
    print(f"{p.nome}: tabela R$ {p.preco:.2f} -> final R$ {p.calcular_preco_final():.2f}")

# ---------- MÉTODOS ----------
print("\n=== MÉTODOS (vender e repor) ===")
iogurte = produtos[1]
total = iogurte.vender(5)
print(f"Vendeu 5 iogurtes: R$ {total:.2f} | estoque agora: {iogurte.estoque}")
iogurte.repor(10)
print(f"Repôs 10 iogurtes | estoque agora: {iogurte.estoque}")

# ---------- HERANÇA ----------
# Todas as filhas usam vender() e repor() que foram escritos SÓ na classe Produto.
print("\n=== HERANÇA ===")
pizza = produtos[4]
print(f"Pizza usou vender() da mãe: R$ {pizza.vender(2):.2f}")
print("Pizza é Produto?", isinstance(pizza, Produto))
print("Pizza é Perecível?", isinstance(pizza, ProdutoPerecivel))

# Métodos que existem SÓ em uma filha:
suco = produtos[3]
print(f"Suco: R$ {suco.preco_por_litro():.2f} por litro (método só do líquido)")

# ---------- ENCAPSULAMENTO ----------
print("\n=== ENCAPSULAMENTO ===")
caderno = produtos[0]
print("Margem (usa o custo privado):", caderno.margem())

try:
    caderno.estoque = -5                       # o setter bloqueia valor inválido
except ValueError as erro:
    print("Setter bloqueou:", erro)

try:
    caderno.vender(999)                        # o método valida a regra de negócio
except ValueError as erro:
    print("vender() bloqueou:", erro)

try:
    print(caderno.__custo)                     # privado: não dá para acessar de fora
except AttributeError:
    print("Não dá para acessar __custo de fora da classe")