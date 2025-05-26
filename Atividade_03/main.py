from carro import Carro

# Criando um carro modelo "Fusca"
meu_carro = Carro("Monza")

# Testando os métodos
meu_carro.mostrar_velocidade()  # Deve mostrar 0
meu_carro.acelerar()
meu_carro.mostrar_velocidade()  # Deve mostrar 10
meu_carro.acelerar()
meu_carro.mostrar_velocidade()  # Deve mostrar 20
meu_carro.frear()
meu_carro.mostrar_velocidade()  # Deve mostrar 10
meu_carro.frear()
meu_carro.frear()               # Tentativa de frear abaixo de 0
meu_carro.mostrar_velocidade()  # Deve mostrar 0
