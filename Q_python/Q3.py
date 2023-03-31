#Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

palavras = ['maça', 'arara', 'audio, radio', 'radar', 'moto']

for palavra in palavras:
    if palavra == palavra[::-1]:
       print(palavra, "é um palíndromo")
    else:
        print(palavra, "não é um palíndromo")    