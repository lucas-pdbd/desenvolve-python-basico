# Questão 1: Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.

num1 = float(input("Digite o primeiro número decimal: "))
num2 = float(input("Digite o segundo número decimal: "))
diferenca_absoluta = abs(num1 - num2)
resultado = round(diferenca_absoluta, 2)
print(f"A diferença absoluta entre {num1} e {num2} é: {resultado}")


# Questão 2: Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n. 
# Biblioteca random: Função randint()
# Biblioteca math:  Função sqrt()

import random
import math

n = int(input("Digite a quantidade de números inteiros aleatórios a serem gerados (n): "))
soma = sum(random.randint(0, 100) for _ in range(n))
raiz_quadrada = math.sqrt(soma)
print(f"A raiz quadrada da soma dos {n} valores aleatórios é: {raiz_quadrada:.2f}") 


# Questão 3: Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.
# Exemplo de interação: 
    # Adivinhe o número entre 1 e 10: 5
    #Muito alto, tente novamente!
    #Adivinhe o número entre 1 e 10: 3
    #Correto! O número é 3.

import random

numero_aleatorio = random.randint(1, 10)
palpite = None

while palpite != numero_aleatorio:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite < numero_aleatorio:
        print("Muito baixo, tente novamente!")
    elif palpite > numero_aleatorio:
        print("Muito alto, tente novamente!")
    else:
        print(f"Correto! O número é {numero_aleatorio}.")       


# Questão 4: Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir: Data: 15/03/2023 Hora: 14:05
# Função datetime.datetime.now() cujo retorno possui os atributos: day, month, year, hour, minute
#Usar a formatação com f-strings no momento de imprimir. Atenção para os atributos que devem sempre ter 2 dígitos precedidos por zero se necessário.

import datetime

data_hora_atual = datetime.datetime.now()
data_formatada = f"Data: {data_hora_atual.day:02d}/{data_hora_atual.month:02d}/{data_hora_atual.year} Hora: {data_hora_atual.hour:02d}:{data_hora_atual.minute:02d}"
print(data_formatada)  


# Questão 5: Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas. Faça:
    # Conheça a função emoji.emojize()
# Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji. Em seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).
import emoji
def listar_emojis():
    emojis = {
        ":smile:": "😄",
        ":heart:": "❤️",
        ":thumbs_up:": "👍",
        ":sunglasses:": "😎",
        ":cry:": "😢",
        ":fire:": "🔥",
        ":rocket:": "🚀",
        ":star:": "⭐"
    }
    print("Emojis disponíveis:")
    for code, symbol in emojis.items():
        print(f"{code} - {symbol}")

listar_emojis()
frase_codificada = input("Digite uma frase codificada com emojis (use os códigos acima): ")
frase_decodificada = emoji.emojize(frase_codificada, use_aliases=True)
print(f"Frase decodificada: {frase_decodificada}")
