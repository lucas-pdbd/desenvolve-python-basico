# Questão 1: Escreva uma função calcula_area_perimetro que recebe apenas um parâmetro dimensoes e calcula a área e o perímetro a partir das dimensões dadas.
# dimensoes é uma tupla (largura, comprimento) com as dimensões de um terreno retangular
#Sua função deve calcular e retornar as seguintes operações:
    #Área = largura * comprimento
    #Perímetro = 2 * (largura + comprimento)
# Implemente aqui a função calcula_area_perimetro:
def calcula_area_perimetro(dimensoes):
    largura, comprimento = dimensoes
    area = largura * comprimento
    perimetro = 2 * (largura + comprimento)
    return area, perimetro  

# Complete o exemplo de uso abaixo
#largura = 5
#comprimento = 7
# retorno = ?
# retorno = calcula_area_perimetro((largura, comprimento))
# print(retorno)  # (35, 24)


# Questão 2: Dada uma string, imprima todas as vogais que aparecem na string, bem como todos os índices onde elas ocorrem. Para isso, use a função enumerate.
frase = "O rato roeu a roupa da Alice"
# Implemente aqui sua solução
vogais = "aeiouAEIOU"
for indice, letra in enumerate(frase):
    if letra in vogais:
        print(f"Vogal: {letra}, Índice: {indice}")      


# Questão 3: Escreva uma função em Python chamada ordenar_tuplas que recebe uma lista de tuplas, cada uma contendo o nome de um aluno e sua respectiva média, e retorna uma nova lista ordenada em ordem decrescente de médias.
# Implemente aqui a função ordenar_tuplas:
def ordenar_tuplas(alunos_notas):
    return sorted(alunos_notas, key=lambda x: x[1], reverse=True)   

# Exemplo de uso:
    # alunos_notas = [('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.0), ('David', 8.8)]
    # resultado = ordenar_tuplas(alunos_notas)
    # print(resultado)
    # Saída esperada: [('Charlie', 9.0), ('David', 8.8), ('Alice', 8.5), ('Bob', 7.2)]


# Questão 4: Escreva uma função em Python chamada comprimir_tuplas que recebe uma lista de tuplas, cada uma contendo uma palavra e um número, e retorna uma nova lista de tuplas onde palavras idênticas são agrupadas e seus números são somados.
# Exemplo de uso:
    # tuplas_originais = [('maçã', 3), ('banana', 2), ('maçã', 5), ('laranja', 1), ('banana', 3)]
    # resultado = comprimir_tuplas(tuplas_originais)
    # print(resultado)
    # Saída esperada: [('maçã', 8), ('banana', 5), ('laranja', 1)]

# Implemente aqui a função comprimir_tuplas:
def comprimir_tuplas(tuplas_originais):
    resultado = {}
    for palavra, numero in tuplas_originais:
        if palavra in resultado:
            resultado[palavra] += numero
        else:
            resultado[palavra] = numero
    return list(resultado.items())  


# Questão 5: Escreva um script que peça o nome e a idade de todos na fila de uma balada. Crie uma lista de tuplas com os pares (nome, idade) de cada um. Em seguida crie e imprima duas tuplas apenas com os nomes, uma com os menores de idade que não poderão entrar, e uma com os maiores de idade (idade >= 18).
# Implemente aqui sua solução:
fila_balada = []
while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = int(input("Digite a idade: "))
    fila_balada.append((nome, idade))   
menores_idade = tuple(nome for nome, idade in fila_balada if idade < 18)
maiores_idade = tuple(nome for nome, idade in fila_balada if idade >= 18)
print("Menores de idade (não podem entrar):", menores_idade)
print("Maiores de idade (podem entrar):", maiores_idade)    








