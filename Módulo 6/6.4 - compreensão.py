# Questão 1: Escreva um script python que use compreensão de listas para criar as seguintes listas:
#Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
#Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
#Todos os números entre 1 e 100 que sejam divisíveis por 7
#Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar'])

pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]
print(pares_20_50)      

quadrados = [x**2 for x in [1,2,3,4,5,6,7,8,9]]
print(quadrados)

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print(divisiveis_por_7)

par_ou_impar = ['par' if x % 2 == 0 else 'impar' for x in range(0, 30, 3)]
print(par_ou_impar) 


# Questão 2: Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase (remova espaços em branco)
# Exemplo:
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

frase = input("Digite uma frase: ")
vogais = sorted([char for char in frase if char.lower() in 'aeiou'])
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']
print("Vogais:", vogais)
print("Consoantes:", consoantes)


# Questão 3: Reescreva o código a seguir para construir a lista pagamentos usando compreensão de listas, ou seja, eliminando o laço de repetição.
# horas_trabalhadas = [40, 37, 45, 40, 40, 48]
# ganho_por_hora = 20
# hora_extra = 25
# pagamentos = []
# for hora in horas_trabalhadas:
    #pagamentos.append(ganho_por_hora * min(hora, 40) + \
                      #hora_extra * max(0, hora-40))

#print(pagamentos)

horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = [ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora-40) for hora in horas_trabalhadas]
print(pagamentos)


# Questão 4: Reescreva o código a seguir para construir a lista aprovados usando compreensão de listas, ou seja, eliminando o laço de repetição.
# alunos = ["Maria", "Jose", "Carla", "Sol"]
# notas = [35, 50, 20, 80]
# aprovados = []
# for i in range(len(notas)):
# if notas[i] >= 60:
# aprovados.append(alunos[i]) 

alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]
print(aprovados)    
