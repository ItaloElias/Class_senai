class Cachorro:
    def __init__(self, nome, raca):
        # Armazena o nome do cachorro
        self.nome = nome
        # Armazena a raça do cachorro
        self.raca = raca

    def latir(self):
        # Imprime a mensagem de latido com o nome e raça do cachorro
        print(f"Au au! Eu sou o {self.nome}, da raça {self.raca}.")
