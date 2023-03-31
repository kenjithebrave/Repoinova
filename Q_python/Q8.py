#Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, 
#False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

class Lampada:
    def __init__(self, estado):
        self.estado = estado

    def liga(self):
        self.estado = True

    def desliga(self):
        self.estado = False

    def esta_ligada(self):
        return self.estado

# cria um objeto Lampada com estado inicial True (ligada)
lampada = Lampada(True)

# liga a lâmpada
lampada.liga()

# verifica se a lâmpada está ligada
print("A lâmpada está ligada?", lampada.esta_ligada())

# desliga a lâmpada
lampada.desliga()

# verifica se a lâmpada ainda está ligada
print("A lâmpada ainda está ligada?", lampada.esta_ligada())