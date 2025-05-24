# nomeação de classe nós usamos CamelCase
class ContaBancaria:
    # construtor da classe 
    # o self é o objeto 
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    # metodos são ações que o objeto pode realizar
    def sacar(valor, self):
        self.saldo = self.saldo - valor

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

    def consultar_saldo(self):
        print(self.__saldo) 
