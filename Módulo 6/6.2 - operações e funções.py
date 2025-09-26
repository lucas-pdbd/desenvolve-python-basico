# Questão 1: Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista

import random
valores = []
for i in range(20):
    valores.append(random.randint(-100, 100))
print("Lista ordenada:", sorted(valores))
print("Lista original:", valores)
print("Índice do maior valor:", valores.index(max(valores)))
print("Índice do menor valor:", valores.index(min(valores)))


# Questão 2: Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:
# A lista elementos
# A soma dos valores da lista
# A média dos valores da lista

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]
print("Lista elementos:", elementos)
print("Soma dos valores:", sum(elementos))
print("Média dos valores:", sum(elementos) / len(elementos))    
print("Número de elementos:", num_elementos)
print("Elementos:", elementos)
print("Soma dos valores:", sum(elementos))
print("Média dos valores:", sum(elementos) / num_elementos)


# Questão 3: Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
# Ambas as listas
# A lista intersecção ordenada
# A quantidade de vezes que cada elemento aparece em cada lista
# Atenção, a lista de intersecções não pode ter duplicatas.

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
interseccao = list(set(lista1) & set(lista2))
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção ordenada:", sorted(interseccao))
for elemento in interseccao:
    print(f"O elemento {elemento} aparece {lista1.count(elemento)} vezes na lista 1 e {lista2.count(elemento)} vezes na lista 2.")  


# Questão 4: Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
# Exemplo de interação via terminal:
# Digite a quantidade de elementos da lista 1: 4
# Digite os 4 elementos da lista 1:
#1
#2
#3
#4

# Digite a quantidade de elementos da lista 2: 6
# Digite os 6 elementos da lista 2:
#5
#6
#7
#8
#9
#10

# Lista intercalada: 1 5 2 6 3 7 4 8 9 10

tamanho1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print(f"Digite os {tamanho1} elementos da lista 1:")
for _ in range(tamanho1):
    lista1.append(int(input())) 
tamanho2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {tamanho2} elementos da lista 2:")
for _ in range(tamanho2):
    lista2.append(int(input())) 
lista_intercalada = []
min_tamanho = min(tamanho1, tamanho2)
for i in range(min_tamanho):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
if tamanho1 > tamanho2:
    lista_intercalada.extend(lista1[min_tamanho:])
else:
    lista_intercalada.extend(lista2[min_tamanho:])
print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))  


