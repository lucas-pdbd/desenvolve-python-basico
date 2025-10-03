# Questão 1: Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
# Exemplo:
    # Digite seu nome: Fulano

    # F
    # Fu
    # Ful
    # Fula
    # Fulan
    # Fulano

nome = input("Digite seu nome: ")
for i in range(len(nome)):
    print(nome[:i+1])


# Questão 2: Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.

primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = primeiro_nome + " " + sobrenome
print("Bem-vindo(a), " + nome_completo + "!")


# Questão 3: Escreva um script que dado uma frase conta os espaços em branco.

frase = input("Digite uma frase: ")
contador_espacos = frase.count(" ")
print("Número de espaços em branco na frase:", contador_espacos)


# Questão 4:     Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.

numero = input("Digite o número: ")
if len(numero) == 8:
    numero = "9" + numero
if len(numero) == 9 and numero[0] == "9":
    numero_formatado = numero[:5] + "-" + numero[5:]
    print("Número completo:", numero_formatado)
else:
    print("Número inválido. Certifique-se de que o número tenha 8 ou 9 dígitos.")   


# Questão 5: Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". 
# Exemplo:
    # Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
    # 19 vogais
    # Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
indices_vogais = [i for i, letra in enumerate(frase) if letra in vogais]
print(f"{len(indices_vogais)} vogais")
print("Índices", indices_vogais)


# Questão 6: Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados. Faça como no exemplo:
# Exemplo:
    # Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
    # Digite a palavra objetivo: amor
    # Anagramas: ["amor", "mora", "ramo", "Roma"]

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
palavra_objetivo_sorted = sorted(palavra_objetivo.lower())
palavras = frase.split()
anagramas = [palavra for palavra in palavras if sorted(palavra.lower()) == palavra_objetivo_sorted]
print("Anagramas:", anagramas)  


# Questão 7: Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. 
# Regras:
    # Chave de criptografia: gere um valor n aleatório entre 1 e 10
    # Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
# Exemplo:
    # nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

    # chave_aleatoria = 5

    # nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']

import random
def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    nomes_cript = []
    for nome in nomes:
        nome_cript = ''
        for char in nome:
            novo_char = chr((ord(char) - 33 + chave_aleatoria) % 94 + 33)
            nome_cript += novo_char
        nomes_cript.append(nome_cript)
    return nomes_cript, chave_aleatoria 
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print("Nomes criptografados:", nomes_criptografados)
print("Chave de criptografia:", chave)  


# Questão 8: Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 
# O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2, como no exemplo abaixo:
# Exemplo:
    # CPF [1 ; 1 ; 1 ; 4 ; 4 ; 4 ; 7 ; 7 ; 7]
    # Multiplicador [10 ; 9 ; 8 ; 7 ; 6 ; 5 ; 4 ; 3 ; 2]
    # Resultado [10 ; 9 ; 8 ; 28 ; 24 ; 20 ; 28 ; 21 ; 14]
    # Soma = 162
# Em seguida, calculamos o módulo 11 da soma (162 % 11 = 8). Se o resultado for menor que 2, o dígito verificador é 0. Caso contrário, o dígito verificador é 11 menos o resultado do módulo (11 - 8 = 3). 
# Repetimos o processo para o segundo dígito verificador, mas agora considerando os primeiros 9 dígitos mais o primeiro dígito verificador (ex: 111.444.777-3) e utilizando multiplicadores crescentes a partir do número 2.
# Exemplo:
    # CPF [1 ; 1 ; 1 ; 4 ; 4 ; 4 ; 7 ; 7 ; 7 ; 3]
    # Multiplicador [11 ; 10 ; 9 ; 8 ; 7 ; 6 ; 5 ; 4 ; 3 ; 2]
    # Resultado [11 ; 10 ; 9 ; 32 ; 28 ; 24 ; 35 ; 28 ; 21 ; 6]
    # Soma = 204
# O dígito verificador é calculado da mesma forma (204 % 11 = 6, então 11 - 6 = 5). 
# Por fim, comparamos os dígitos verificadores calculados com os dígitos verificadores fornecidos no CPF. Se ambos coincidirem, o CPF é válido; caso contrário, é inválido. 

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
cpf_numeros = cpf.replace(".", "").replace("-", "") 
if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
    print("Inválido")
else:
    def calcular_digito_verificador(cpf_parcial):
        soma = sum(int(digito) * multiplicador for digito, multiplicador in zip(cpf_parcial, range(len(cpf_parcial)+1, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    primeiro_digito = calcular_digito_verificador(cpf_numeros[:9])
    segundo_digito = calcular_digito_verificador(cpf_numeros[:9] + primeiro_digito)
    if cpf_numeros[-2:] == primeiro_digito + segundo_digito:
        print("Válido")
    else:
        print("Inválido")   


