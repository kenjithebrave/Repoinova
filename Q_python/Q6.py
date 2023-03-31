#Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo. 
# Você deve criar um arquivo .txt na pasta do seu repositório e inserir seu nome, idade e ano de inicio do curso 
# dentro dele com quebra de linhas por informação

# Abrir o arquivo e imprimir o conteúdo na tela
'''
arq = open('arquivoq6.txt', 'r')
print(arq)
'''

with open("Q_python/arquivoq6.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

    
