"""
2. Encapsulamento (e o @property)
O problema que ele resolve

Sem proteção, qualquer parte do programa pode quebrar o objeto:

Encapsulamento significa colocar um guarda na porta: ninguém altera o dado sem passar pelas regras da classe.

Passo 1: a primeira ideia, o método guardião

Podemos proibir a alteração direta e só permitir por métodos:

python
p.vender(2)     # dentro do método existem as validações

O problema é que ainda dá para fazer p.estoque = -500 direto. Falta fechar essa porta.

Passo 2: a convenção do _
python
self._estoque = 40

O underline avisa: “isto é interno, não mexa direto”. O Python não bloqueia (é só um combinado entre programadores), mas quem lê o código entende.

Passo 3: o @property

Agora queremos o melhor dos dois mundos:

Quem usa a classe escreve p.estoque (simples, como um atributo normal).
Por baixo, uma função roda e valida.

É exatamente isso que o @property faz.
"""

class Produto:
    def __init__(self, nome, estoque):
        self.nome = nome
        self._estoque = 0
        self.estoque = estoque        # passa pelo setter (validado!)

    @property
    def estoque(self):                # chamado quando você LÊ
        return self._estoque

    @estoque.setter
    def estoque(self, valor):         # chamado quando você ESCREVE
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        self._estoque = valor

class Pao(Produto):
    pass
p = Produto("Caderno", 40)
print(p.nome)
print(p.estoque)
p.estoque = 90
print(p.nome)
print(p.estoque)

b = Pao
b.nome = "Pão de forma"
b.estoque = 45
print(b.nome)
print(b.estoque)

"""
O que o @property realmente faz

Ele “disfarça” uma função de atributo. Veja o que o Python executa de verdade:

Você escreve	O Python executa
print(p.estoque)	a função marcada com @property (o getter)
p.estoque = 10	a função marcada com @estoque.setter (o setter)

Os parênteses nunca aparecem, mas há uma função rodando.

Os dois nomes: estoque e _estoque

São duas coisas diferentes:

_estoque é o cofre: onde o número fica guardado de verdade.
estoque é a portinha com o guarda: o que o mundo de fora usa.


"""