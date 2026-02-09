class Carro:
    def __init__(self, modelo, cor, ano, km, peso, preco):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.km = km
        self.peso = peso
        self.preco = preco
        self.ligado = False
        self.seta = None

    def exibir_caracteristicas(self):
        print(f'Modelo: {self.modelo}\n'
              f'Cor: {self.cor}\n'
              f'ano: {self.ano}\n'
              f'km: {self.km}Km\n'
              f'Peso: {self.peso:.2f}KG\n'
              f'Preco: R${self.preco:.2f}')

    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            print("O carro já estava ligado")

    def desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            print("O carro já estava desligado")

    def dar_seta(self, direcao):

        if self.ligado:
            if direcao == 'Esquerda':
                self.seta = direcao
                print("Tuc tuc tuc Esquerda")
            elif direcao == 'Direta':
                self.seta = direcao
                print("Tuc tuc tuc Direita")
            else:
                print("Direção invalida")
        else:
            print("Ligue o carro")

lista_de_carros = []

        # Caracteristicas do carro
def construcao_carro():
    modelo_do_carro = input("Digite o modelo do carro: ")
    cor_do_carro = input("Digite o cor do carro: ")
    ano_do_carro = int(input("Digite o ano do carro: "))
    km_do_carro = float(input("Digite o km do carro: "))
    peso_do_carro = float(input("Digite o peso do carro: "))
    preco_do_carro = float(input("Digite o preco do carro: "))
    car = Carro(modelo_do_carro, cor_do_carro, ano_do_carro, km_do_carro, peso_do_carro, preco_do_carro)
    lista_de_carros.append(car)

construcao_carro()

lista_de_carros[0].exibir_caracteristicas()
lista_de_carros[0].ligar()
lista_de_carros[0].ligar()
lista_de_carros[0].desligar()
lista_de_carros[0].desligar()
lista_de_carros[0].dar_seta('Esquerda')
lista_de_carros[0].ligar()
lista_de_carros[0].dar_seta('Direta')
lista_de_carros[0].dar_seta('Frente')


for index, carro in enumerate(lista_de_carros):
    print("-="*20)
    print(f"{index + 1}: ")
    carro.exibir_caracteristicas()
    print('-='*20)