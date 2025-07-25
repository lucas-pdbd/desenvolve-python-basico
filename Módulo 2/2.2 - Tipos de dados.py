#Qustão 1: Transforme o seguinte algoritmo em código. Lembre-se das funções print e type que já conhecemos de forma geral.
    #1-Armazene o valor 5 em uma variável e o valor 2 em outra variável;

    #2-Imprima o tipo de dados dessas duas variáveis;

    #3-Divida a primeira variável (com o valor 5) pela segunda variável (com o valor 2) e armazene o resultado em uma terceira variável;

    #4-Imprima a terceira variável e também o seu tipo.
a = 5
b = 2
print (type(a),type(b))
c = a / b
print (c)
print(type(c))

#Questão 2: Transforme o seguinte algoritmo em código. Lembre-se das funções print e type que já conhecemos de forma geral.
    #1-Armazene o texto "o resultado é"  em uma variável, o valor 10 em outra variável, e o valor 3.5 numa terceira variável.

    #2-Some os valores da segunda e terceira variável e armazene em outra variável.

    #3-Imprima todas as variáveis na ordem de criação e imprima também seus tipos.
texto = 'o resultado é:'
a = 10
b = 3.5
c = a + b 
print (texto, a, b, c)
print(type(texto), type(a), type(b), type(c))

#Questão 3: Dadas duas variáveis v1 = 10 e v2 = 20, utilize uma terceira variável para trocar os valores entre as duas variáveis. Ou seja, ao final v1 terá o valor de v2, e v2 o valor de v1. Você deve usar uma variável auxiliar de troca, não podendo atribuir os novos valores diretamente.
v1 = 10
v2 = 20
aux = v1
v1 = v2
v2 = aux
print("v1:", v1)
print("v2:", v2)

#Questão 4:  Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. Reescreva esse código usando apenas duas variáveis.
# juros = 1.01
# saldo = 500.0
# rendimento1 = saldo * juros
# rendimento2 = rendimento1 * juros
# rendimento3 = rendimento2 * juros
# print("Após 3 meses meu novo saldo é")
# print(rendimento3)

juros = 1.01
saldo = 500.0
saldo *= juros
saldo *= juros
saldo *= juros
print("Após 3 meses meu novo saldo é")
print(saldo)


 


