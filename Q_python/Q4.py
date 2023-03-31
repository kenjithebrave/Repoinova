#Dada as listas a seguir, faça um programa que imprima o dados na seguinte estrutura: 
# "índice - primeiroNome sobreNome está com idade anos". primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']  
# sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira'] idades = [19, 28, 25, 31]

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, (primeiroNome, sobreNome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{i} - {primeiroNome} {sobreNome} está com {idade} anos.")