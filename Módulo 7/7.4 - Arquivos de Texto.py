# Questão 1: Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo. Faça como no exemplo abaixo:
# Exemplo:
    # Digite uma frase: Bom dia, meu nome é Davi.
    # Frase salva em /Users/laranjeira/python-basico/frase.txt

import os   
frase = input("Digite uma frase: ")
caminho_arquivo = os.path.join(os.getcwd(), "frase.txt")
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write(frase)
print(f"Frase salva em {caminho_arquivo}")  


# Questão 2: Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt". Faça como no exemplo abaixo:
# Exemplo:
    # Bom
    # dia
    # meu
    # nome
    # é
    # Davi

import os
import re   
caminho_arquivo_frase = os.path.join(os.getcwd(), "frase.txt")
caminho_arquivo_palavras = os.path.join(os.getcwd(), "palavras.txt")    
with open(caminho_arquivo_frase, "r") as arquivo_frase:
    conteudo = arquivo_frase.read()
    palavras = re.findall(r'\b\w+\b', conteudo)
with open(caminho_arquivo_palavras, "w") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")
with open(caminho_arquivo_palavras, "r") as arquivo_palavras:
    conteudo_palavras = arquivo_palavras.read()
    print(conteudo_palavras)    


# Questão 3:     Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt". Em seguida crie um script em Python que abra o arquivo para leitura e imprima: O texto das primeiras 25 linhas; O número de linhas do arquivo; A linha com maior número de caracteres; O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

import os
caminho_arquivo_estomago = os.path.join(os.getcwd(), "estomago.txt")    
with open(caminho_arquivo_estomago, "r", encoding="utf-8    ") as arquivo_estomago:
    linhas = arquivo_estomago.readlines()
    print("Primeiras 25 linhas:")
    for linha in linhas[:25]:
        print(linha.strip())
    numero_linhas = len(linhas)
    print(f"Número de linhas: {numero_linhas}")
    linha_mais_longa = max(linhas, key=len).strip()
    print(f"Linha com maior número de caracteres: {linha_mais_longa}")
    conteudo_completo = ''.join(linhas).lower()
    mencoes_nonato = conteudo_completo.count("nonato")
    mencoes_iria = conteudo_completo.count("íria")
    print(f"Número de menções a 'Nonato': {mencoes_nonato}")
    print(f"Número de menções a 'Íria': {mencoes_iria}")    


# Questão 4: Vamos fazer o jogo da forca! Antes de programar: 
# Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
# Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.
# Escreva um programa em Python para executar o jogo, de acordo com as definições:
# Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
# Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
# No início exiba o número de letras na palavra como underscores;
# Permita que o jogador insira letras para adivinhar a palavra;
# Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
# Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
# Limite o número de tentativas para 6 (as partes do enforcado).

import os
import random   
caminho_arquivo_gabarito = os.path.join(os.getcwd(), "gabarito_forca.txt")
caminho_arquivo_enforcado = os.path.join(os.getcwd(), "gabarito_enforcado.txt")    
with open(caminho_arquivo_gabarito, "r") as arquivo_gabarito:
    palavras = [linha.strip() for linha in arquivo_gabarito.readlines()]
palavra_secreta = random.choice(palavras).lower()
with open(caminho_arquivo_enforcado, "r") as arquivo_enforcado:
    estagios_enforcado = [linha.strip() for linha in arquivo_enforcado.readlines() if linha.strip()]
tentativas = 6
letras_adivinhadas = []
def imprime_enforcado(erros):
    print(estagios_enforcado[erros])
while tentativas > 0:   
    progresso = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])
    print(f"Palavra: {progresso}")
    if '_' not in progresso:
        print("Parabéns! Você adivinhou a palavra!")
        break
    letra = input("Digite uma letra: ").lower()
    if letra in letras_adivinhadas:
        print("Você já tentou essa letra. Tente outra.")
        continue
    letras_adivinhadas.append(letra)
    if letra not in palavra_secreta:
        tentativas -= 1
        print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")
        imprime_enforcado(6 - tentativas)
    if tentativas == 0:
        print(f"Você perdeu! A palavra era: {palavra_secreta}") 


# Questão 5: A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.
# Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
# No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
# Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
# A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
# Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.
import os   
caminho_arquivo_livros = os.path.join(os.getcwd(), "meus_livros.csv")
livros = [
    {"Título": "livro1", "Autor": "irineu", "Ano de publicação": 1956, "Número de páginas": 158},
    {"Título": "livro2", "Autor": "irineujr", "Ano de publicação": 1986, "Número de páginas": 254},
]
with open(caminho_arquivo_livros, "w") as arquivo_livros:
    arquivo_livros.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        linha = f"{livro['Título']},{livro['Autor']},{livro['Ano de publicação']},{livro['Número de páginas']}\n"
        arquivo_livros.write(linha)
print(f"Arquivo salvo em {caminho_arquivo_livros}") 
# Agora abra o arquivo "meus_livros.csv" com o Google Sheets ou outro software de planilhas e veja como ficou.  


# Questão 6:     Vamos descobrir as músicas mais populares do Spotify nos últimos 10 anos! 
# Crie uma conta no Kaggle, uma das principais plataformas de ciência de dados e aprendizado de máquina. Em disciplinas avançadas vamos trabalhar com bases de dados provenientes de lá!
# Baixe o arquivo spotify-2023.csv no final da página que apresenta os dados.
# No Python, abra o arquivo para leitura e imprima as cinco primeiras linhas
# Para abrir o arquivo, defina o parâmetro encoding='latin-1'
# Após compreender a estrutura do arquivo (divisão em colunas, caracter separador de coluna, etc.) passamos para a etapa de extração de informações.
# O arquivo está estruturado da seguinte forma: cada linha representa uma música e contém as seguintes informações separadas por vírgula (CSV):
# track_name,artist(s)_name,artist_count,released_year,released_month,released_day,in_spotify_playlists,in_spotify_charts,streams,in_apple_playlists
# Usaremos apenas informações das colunas:
    #track_name   Nome da música
    #artist(s)_name  Nome do artista
    #artist_count   Número de artistas listados em artist(s)_name
    #released_year   Ano de lançamento
    #streams   Número de vezes que a música foi tocada no Spotify
# Você deve criar um script Python para processar esse arquivo e gerar uma lista com 10 elementos, cada qual representando a música mais tocada de cada ano no intervalo de 2012 a 2022. Considere somente músicas dentro do intervalo solicitado. Cada elemento da lista produzida deve conter as seguintes informações:
# [track_name, artist(s)_name, released_year, streams]
# Essa atividade tem alguns desafios. Assim como as colunas da tabela são separadas por vírgulas, músicas com mais de um artista (artist_count>1) terá o campo artist(s)_name entre aspas com o nome dos artistas separado por vírgulas. Ex:
# Seven (feat. Latto) (Explicit Ver.),"Latto, Jung Kook",2,2023, …
# Há também nomes de músicas entre aspas por conter caracteres especiais como vírgulas ou aspas. Ex:
# "Peso Pluma: Bzrp Music Sessions,Vol.55","Bizarrap,Peso Pluma",2,2023,
# Você deve ignorar essas linhas, e terá portanto que propor uma verificação para identificá-las.
# Ao final imprima a lista produzida. Ex:
#[['When I Was Your Man', 'Bruno Mars', 2012, 1661187319], 
# ['I Wanna Be Yours', 'Arctic Monkeys', 2013, 1297026226], 
# ...,
# ['As It Was', 'Harry Styles', 2022, 2513188493]]
# Observção: o 'archive.zip' contém o arquivo 'spotify-2023.csv' compactado. Você deve descompactá-lo antes de usar.
import os
caminho_arquivo_spotify = os.path.join(os.getcwd(), "spotify-2023.csv")    
musicas_mais_tocadas = {}
with open(caminho_arquivo_spotify, "r", encoding="latin-1") as arquivo_spotify:
    next(arquivo_spotify)  
    for linha in arquivo_spotify:
        partes = linha.strip().split(',')
        if len(partes) < 10 or '"' in partes[0] or '"' in partes[1]:
            continue
        track_name = partes[0]
        artist_name = partes[1]
        released_year = int(partes[3])
        streams = int(partes[8])
        if 2012 <= released_year <= 2022:
            if released_year not in musicas_mais_tocadas or streams > musicas_mais_tocadas[released_year][3]:
                musicas_mais_tocadas[released_year] = [track_name, artist_name, released_year, streams]
lista_musicas = [musicas_mais_tocadas[ano] for ano in range(2012, 2023) if ano in musicas_mais_tocadas]
print(lista_musicas)    


