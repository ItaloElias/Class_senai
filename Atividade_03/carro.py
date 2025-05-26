class Carro:
    def __init__(self, modelo):
        # Atributo do modelo do carro
        self.modelo = modelo
        # Velocidade inicial é sempre 0
        self.velocidade = 0

    # Método para aumentar a velocidade em 10
    def acelerar(self):
        self.velocidade += 10

    # Método para diminuir a velocidade em 10, sem ir abaixo de 0
    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            self.velocidade = 0

    # Método para exibir a velocidade atual
    def mostrar_velocidade(self):
        print(f"Velocidade atual do {self.modelo}: {self.velocidade} km/h")
