class Funcionario:
    def __init__(self, nome, idade, salario, cargo):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.cargo = cargo
    def informacoes_funcionario(self):
        print(f"Nome: {self.nome}\n"
              f"Idade: {self.idade}\n"
              f"Salario: R${self.salario:.2f}\n"
              f"Cargo: {self.cargo}\n")
    def mudar_cargo(self, cargo):
        self.cargo = cargo

    def atualizar_idade(self, nova_idade):
        if nova_idade < self.idade or nova_idade == self.idade:
            print("A nova idade não pode ser igual ou menor que a antiga")
        else:
            self.idade = nova_idade

funcionario = Funcionario("Hugo", 22, 14000, "Engenheiro de IA (Junior)")
funcionario.mudar_cargo("Engenheiro e IA (Pleno)")
funcionario.atualizar_idade(23)
funcionario.informacoes_funcionario()

