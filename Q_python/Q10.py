with open('numbers.txt', 'r') as f:
    # lê todas as linhas do arquivo e cria uma lista de inteiros
    numeros = list(map(int, f.readlines()))

# filtra somente os números pares e os ordena em ordem decrescente
pares = sorted(filter(lambda x: x % 2 == 0, numeros), reverse=True)

# seleciona somente os 5 maiores valores pares
maiores_pares = pares[:5]

# calcula a soma dos 5 maiores valores pares
soma_maiores_pares = sum(maiores_pares)

# imprime o resultado
print("Os 5 maiores valores pares são:", maiores_pares)
print("A soma dos 5 maiores valores pares é:", soma_maiores_pares)

# Fiquei na dúvida se criava um arquivo txt com os números pra testar mas no final decidi só deixar assim mesmo