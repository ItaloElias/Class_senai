from produto import Produto

produto1 = Produto("Caneta", 1.50, 100)

produto1.mostrar_estoque()  # Mostra estoque inicial: 100
produto1.comprar(20)         # Compra 20 unidades
produto1.mostrar_estoque()  # Mostra estoque: 80
produto1.comprar(100)        # Tenta comprar mais que estoque disponível
produto1.repor(50)           # Reposição de 50 unidades
produto1.mostrar_estoque()  # Mostra estoque final
