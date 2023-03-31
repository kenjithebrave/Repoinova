#Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo. 
# Você deve criar um arquivo .txt na pasta do seu repositório e inserir seu nome, idade e ano de inicio do curso 
# dentro dele com quebra de linhas por informação

# Abrir o arquivo e imprimir o conteúdo na tela
with open("arquivo_texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Criar um arquivo e escrever as informações
nome = "Silas Kenji"
idade = 20
ano_inicio_curso = 2023

with open("arquivo_texto.txt", "w") as arquivo:
    arquivo.write(nome + "\n")
    arquivo.write(str(idade) + "\n")
    arquivo.write(str(ano_inicio_curso) + "\n")
    
#obs: essa aqui realmente me pegou de jeito, por mais que não seja algo complexo utiliza algumas funções do python com as quais n estou mto acostumado
#ent acabei puxando uma ajudinha do stackoverflow, ainda vou reestruturar ela da minha maneira quando estiver com mais tempo     
    