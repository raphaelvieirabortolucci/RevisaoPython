# count
# conta quantas vezes um elemento se repete

lista = [1, 2, 3, 4, 2, 5, 2, 6]  
print("esse numero se repete:", lista.count(2), "vezes") #conta quantas vezes o numero 2 aparece

#copy
#copia a lista, criando uma nova
lista2 = lista.copy()

#reverse
#inverte a ordem da lista

lista2.reverse()
print("lista copiada invertidaL:", lista2)

#sort
#ordena a lista de forma crescente
lista.sort()
print("os numeros de ordem crescente:", lista)

#ordena de forma decrescente

lista.sort(reverse=True)
print("lista decresente:", lista)

print("o tamanho da lista é:", len(lista2)) # tamanho da lista
print("o maior numero da lista é:", max(lista2)) # maior numero da lista
print("o menor numero da lista é:", min(lista2)) # menor numero da lista
print("a soma dos numeros da lista é:", sum(lista2)) # soma da lista
