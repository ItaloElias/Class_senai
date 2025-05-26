class CalculadoraSimples:
    def somar(self, a, b):
        # Calcula a soma e imprime o resultado
        resultado = a + b
        print("Soma:", resultado)

    def subtrair(self, a, b):
        # Calcula a subtração e imprime o resultado
        resultado = a - b
        print("Subtração:", resultado)

    def multiplicar(self, a, b):
        # Calcula a multiplicação e imprime o resultado
        resultado = a * b
        print("Multiplicação:", resultado)

    def dividir(self, a, b):
        # Verifica divisão por zero e imprime o resultado ou mensagem de erro
        if b == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            resultado = a / b
            print("Divisão:", resultado)
