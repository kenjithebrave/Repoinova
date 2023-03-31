# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
# Depois imprima a soma dos valores. texto = "1,3,4,6,10,76"

def soma_numeros(texto):
    numeros = texto.split(",")
    soma = sum(map(int, numeros))
    print("A soma dos números é:", soma)

# Exemplo:
texto = "1,3,5,7,69,79"
soma_numeros(texto)