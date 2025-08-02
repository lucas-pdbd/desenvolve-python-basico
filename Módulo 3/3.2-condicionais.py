# Questão 1: Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.

num1 = int(input("Digite o primeiro número: ")) 
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2          
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")


# Questão 2: Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme: Se a avaliação for 5, imprima "Excelente!"; Se a avaliação for 4, imprima "Muito Bom!"; Se a avaliação for 3, imprima "Bom!"; Se a avaliação for 2, imprima "Regular."; Se a avaliação for 1, imprima "Ruim.".

avaliacao = int(input("Digite a avaliação do filme (1 a 5): "))
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, insira um número entre 1 e 5.") 


# Questão 3: Você está desenvolvendo um programa para verificar se um ano é bissexto. Escreva um código em Python que solicita ao usuário para inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto". 

ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")   


# Questão 4: Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:  
    # Distância até 100 km: R$1 por kg;
    # Distância entre 101 e 300 km: R$1.50 por kg;
    # Distância acima de 300 km: R$2 por kg;
    # Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg.

distancia = float(input("Digite a distância da entrega em km: "))
peso = float(input("Digite o peso do pacote em kg: "))
if distancia <= 100:
    frete = peso * 1
elif 101 <= distancia <= 300:
    frete = peso * 1.50
else:
    frete = peso * 2        
if peso > 10:
    frete += 10
print(f"O valor do frete é R${frete:.2f}")