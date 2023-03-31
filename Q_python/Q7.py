# Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados
#e imprime o valor de cada parâmetro recebido. Dica: pesquise sobre *args e **kwargs.    
# Aplique os seguintes parâmetros: a = (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)


def imprimir_parametros(*args, **kwargs):
    print("Argumentos não nomeados:")
    for arg in args:
        print(arg)
    print("Argumentos nomeados:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


a = (1, 3, 4, 'hello')
parametro_nomeado = 'algo'
x = 20

imprimir_parametros(*a, parametro_nomeado=parametro_nomeado, x=x)