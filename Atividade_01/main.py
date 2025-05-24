from conta import ContaBancaria

# criar/instanciar objeto
conta_1 = ContaBancaria("Italo", 0)
conta_2 = ContaBancaria("Yasmin", 0)

conta_1.depositar(3000)
conta_1.sacar(1500)
conta_1.consultar_saldo()

conta_2.consultar_saldo()
