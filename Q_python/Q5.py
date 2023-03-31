#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.
# Lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def remover_duplicados(lista):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_sem_duplicatas = remover_duplicados(lista)
print(lista_sem_duplicatas)
