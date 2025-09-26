# Questão 1: Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )
# Solicita ao usuário uma quantidade indefinida de números inteiros

numeros = []
while True:
    entrada = input("Digite um número inteiro (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, insira pelo menos 4 números antes de sair.")
            continue
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])


# Questão 2: Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios, conforme exemplo a seguir. 
# URLs: ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
# dominios:  ["google", "gmail", "github", "reddit", "yahoo"] 

urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = [url[4:-4] for url in urls]
print("Domínios:", dominios)


# Questão 3: Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.
# Exemplo:
# Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
# Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

import random
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)   

max_negativos = 0
start_index = -1
end_index = -1
current_start = -1
current_count = 0   
for i, num in enumerate(lista):
    if num < 0:
        if current_start == -1:
            current_start = i
        current_count += 1
    else:
        if current_count > max_negativos:
            max_negativos = current_count
            start_index = current_start
            end_index = i
        current_start = -1
        current_count = 0
if current_count > max_negativos:
    start_index = current_start
    end_index = len(lista)
if start_index != -1 and end_index != -1:
    del lista[start_index:end_index]
print("Editada:", lista)









