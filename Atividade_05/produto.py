class Produto:
    def __init__(self, nome, preco, estoque):
        # Nome do produto
        self.nome = nome
        # Preço do produto
        self.preco = preco
        # Quantidade atual em estoque
        self.estoque = estoque

    def comprar(self, qtd):
        # Reduz o estoque pela quantidade comprada,
        # mas não permite que o estoque fique negativo
        if qtd <= self.estoque:
            self.estoque -= qtd
            print(f"Compra realizada: {qtd} unidades de {self.nome}.")
        else:
            print(f"Estoque insuficiente! Estoque atual: {self.estoque} unidades.")

    def repor(self, qtd):
        # Aumenta o estoque pela quantidade reposta
        self.estoque += qtd
        print(f"Reposto {qtd} unidades de {self.nome}.")

    def mostrar_estoque(self):
        # Imprime a quantidade atual em estoque
        print(f"Estoque atual de {self.nome}: {self.estoque} unidades.")
