# Questão 1: Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Dica: usando listas você não precisa fazer um "if" para cada mês.

data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split('/') 
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes_extenso = meses[int(mes) - 1]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")   


# Questão 2: Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
frase_modificada = ''.join(['*' if char in vogais else char for char in frase])
print("Frase modificada:", frase_modificada)    


# Questão 3: Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".

import string   
while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break
    frase_limpa = ''.join(char.lower() for char in frase if char.isalnum())
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')    


# Questão 4: Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios: Pelo menos 8 caracteres de comprimento ; Contém pelo menos uma letra maiúscula e uma letra minúscula; Contém pelo menos um número; Contém pelo menos um caractere especial (por exemplo, @, #, $).

def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not any(char.islower() for char in senha):
        return False
    if not any(char.isupper() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char in string.punctuation for char in senha):
        return False
    return True 
senha = input("Digite uma senha para validação: ")
if validador_senha(senha):
    print("Senha válida.")
else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.") 


# Questão 5: Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. Dica: use a biblioteca random.

import random   
def embaralhar_palavras(frase):
    def embaralhar(palavra):
        if len(palavra) <= 3:
            return palavra
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)
frase = input("Digite uma frase para embaralhar as palavras: ")
frase_embaralhada = embaralhar_palavras(frase)
print("Frase com palavras embaralhadas:", frase_embaralhada)    

