class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def caracteristicas_da_casa(self):
        print(f'A cor da casa é {self.cor}\n'
              f'A quantidade de quartos da casa é {self.quartos}\n'
              f'A quantidade de banheiros da casa é {self.banheiros}')

    def adicionar_quartos(self, quantidade):
        self.quartos += quantidade

    def trocar_cor_da_casa(self, nova_cor):
        self.cor = nova_cor

casa1 = Casa('Azul', 8, 4)
casa1.adicionar_quartos(6)
casa1.trocar_cor_da_casa("Amarelo")
casa1.caracteristicas_da_casa()