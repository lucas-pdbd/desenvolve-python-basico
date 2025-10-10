# Questão 1: Escreva uma função em Python chamada contagem_caracteres que recebe uma string como parâmetro e retorna um dicionário onde as chaves são os caracteres presentes na string e os valores são a contagem de cada caractere.
# Exemplo de uso:
    # frase = "python programming"
    # resultado = contagem_caracteres(frase)
    #print(resultado)
# Implemente aqui a função contagem_caracteres:
def contagem_caracteres(frase):
    contagem = {}
    for char in frase:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1
    return contagem 
# Testando a função
frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)    


# Questão 2: Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt".
# https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt
# Escreva um script python que abre o arquivo de texto e cria um dicionário contando a quantidade de vezes que cada palavra aparece no texto.
# Em seguida ordene o dicionário de forma decrescente pelos valores. Dessa maneira ele irá apresentar as palavras mais frequentes no início.
# Apresente na tela o dicionário ordenado
# Implemente aqui sua solução:
def contar_palavras_arquivo(estomago):
    with open(estomago, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read().lower()  # Lê o conteúdo do arquivo e converte para minúsculas
        palavras = texto.split()  # Divide o texto em palavras

    contagem_palavras = {}
    for palavra in palavras:
        palavra = palavra.strip('.,!?;"()[]{}')  # Remove pontuação ao redor das palavras
        if palavra:  # Verifica se a palavra não está vazia
            if palavra in contagem_palavras:
                contagem_palavras[palavra] += 1
            else:
                contagem_palavras[palavra] = 1

    # Ordena o dicionário por valores em ordem decrescente
    contagem_ordenada = dict(sorted(contagem_palavras.items(), key=lambda item: item[1], reverse=True))
    return contagem_ordenada   
# Testando a função
estomago = "estomago.txt"
resultado = contar_palavras_arquivo(estomago)
print(resultado)    


# Questão 3: Crie uma função chamada mesclar_dicionarios que recebe dois dicionários como parâmetros e retorna um novo dicionário contendo a fusão dos dois. Se houver chaves comuns, o maior valor deve prevalecer.
# Exemplo de uso:
    # dicionario1 = {'a': 1, 'b': 2, 'c': 3}
    # dicionario2 = {'b': 4, 'd': 5}
    # resultado = mesclar_dicionarios(dicionario1, dicionario2)
    # print(resultado)
    # Saída esperada: {'a': 1, 'b': 4, 'c': 3, 'd': 5}
# Implemente aqui a função mesclar_dicionarios:
def mesclar_dicionarios(dicionario1, dicionario2):
    resultado = dicionario1.copy()  # Começa com uma cópia do primeiro dicionário
    for chave, valor in dicionario2.items():
        if chave in resultado:
            resultado[chave] = max(resultado[chave], valor)  # Mantém o maior valor para chaves comuns
        else:
            resultado[chave] = valor  # Adiciona novas chaves
    return resultado
# Testando a função
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5   }
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)        


# Questão 4: Desenvolva uma função em Python chamada filtrar_dicionario que recebe um dicionário e uma lista de chaves como parâmetros e retorna um novo dicionário contendo apenas as chaves que estão presentes na lista.
# Exemplo de uso:
    # dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    # chaves_filtradas = ['a', 'c', 'e']
    # resultado = filtrar_dicionario(dados, chaves_filtradas)
    # print(resultado)
    # Saída esperada: {'a': 1, 'c': 3, 'e': 5}
# Implemente aqui a função filtrar_dicionario:
def filtrar_dicionario(dados, chaves_filtradas):
    resultado = {chave: dados[chave] for chave in chaves_filtradas if chave in dados}
    return resultado
# Testando a função
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)    


# Questão 5: Você está responsável por analisar os resultados de uma votação. Cada voto é representado por um dicionário com o nome do candidato e a quantidade de votos que recebeu em uma determinada sessão eleitoral. Escreva uma função chamada resultado_votacao que recebe uma lista de dicionários de votos e retorna um dicionário onde as chaves são os nomes dos candidatos, e os valores são tuplas (total, percentual) com o total de votos recebidos por cada candidato e o percentual em relação à soma total de votos em todos os candidatos.
# Exemplo de uso:
    # votos = [
        # {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
        # {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
        # {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
    #]
    # resultado = resultado_votacao(votos)
    # print(resultado) 
    # Saída esperada: {'candidato_A': (360, 40.31), 'candidato_B': (258, 28.89), 'candidato_C': (275, 30.79)}
# Implemente aqui a função resultado_votacao
def resultado_votacao(votos):
    total_votos = {}
    soma_total = 0

    # Soma os votos de cada candidato
    for voto in votos:
        for candidato, quantidade in voto.items():
            if candidato in total_votos:
                total_votos[candidato] += quantidade
            else:
                total_votos[candidato] = quantidade
            soma_total += quantidade

    # Calcula o percentual de votos para cada candidato
    resultado = {candidato: (quantidade, round((quantidade / soma_total) * 100, 2)) for candidato, quantidade in total_votos.items()}
    return resultado
# Testando a função
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)    





