def conta_vogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    qtd_vogais = len(list(filter(lambda x: x.lower() in vogais, texto)))
    return qtd_vogais

#Exemplo teste
texto = "Busco sexo sem compromisso"
qtd_vogais = conta_vogais(texto)
print(f"A frase '{texto}' possui {qtd_vogais} vogais.")