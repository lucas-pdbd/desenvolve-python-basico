# Questão 1: Transforme em código o fluxograma a seguir:
# Passo 1: Leia x; Passo 2: Verifique se x é maior que 5; Passo 3: Se não for, imprima "Fim" ;Passo 4: Se for, imprima "Maior que 5" e em seguida imprima "Fim".

x = int(input("Digite um número: "))
while x > 5:
    print("Maior que 5")
    break

print("Fim")    


# Questão 2: Transforme em código o fluxograma a seguir:
# Passo 1: Leia n; Passo 2: cont = 0; Passo 3: Enquanto n for maior que cont, cont = cont+1, imprima cont; Passo 4: Se n for menor que cont, imprima "Fim".

n = int(input("Digite um número: "))
cont = 0
while n > cont:
    cont += 1
    print(cont)     
print("Fim") 


# Questão 3: Transforme em código o fluxograma a seguir:
# Passo 1: Leia n1, n2, n3; Passo 2: m = (n1+n2+n3)/3; Passo 3: Se m for maior ou igual a 60, imprima "Aprovado"; Passo 4: Se m for maior ou igual a 40 e menor que 60, imprima "Recuperação"; Passo 5: Se m for menor que 40, imprima "Reprovado"; Passo 6: Imprima "Fim".

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
m = (n1 + n2 + n3) / 3  
if m >= 60:
    print("Aprovado")
elif 40 <= m < 60:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")


# Questão 4: Transforme em código o fluxograma a seguir:
# Passo 1: Leia n; Passo 2: maior = 0; Passo 3: Se n for menor que 0, imprima maior, se n for maior que 0, leia x; Passo 4: Se x > maior, maior = x; Passo 5: Se x < maior, n = n-1; Passo 6: Volte para o passo 3.

n = int(input("Digite a quantidade de números que deseja comparar: "))
maior = 0
while n > 0:
    x = int(input("Digite um número: "))
    if x > maior:
        maior = x
    n -= 1
print("O maior número é:", maior)   


# Qustão 5: Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades. (idade1 + idade2 + idade3 + … + idade_n)/N. Utilize o comando while para resolver este problema.

N = int(input("Digite a quantidade de respondentes: "))
soma_idades = 0
contador = 0

while contador < N:
    idade = int(input("Digite a idade do respondente: "))
    soma_idades += idade
    contador += 1

media_idades = soma_idades / N
print("A média das idades é:", media_idades)    


# Questão 6: Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 
#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).
#Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas.

N = int(input("Digite a quantidade de experimentos registrados: "))
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

contador = 0
while contador < N:
    entrada = input("Digite a quantidade de cobaias e o tipo (S, R, C): ").split()
    quantia = int(entrada[0])
    tipo = entrada[1].upper()
    
    total_cobaias += quantia
    
    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia
    
    contador += 1

percentual_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0

print(f"Total de cobaias: {total_cobaias}")
print(f"Total de sapos: {total_sapos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")  

