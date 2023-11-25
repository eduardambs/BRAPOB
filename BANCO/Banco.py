# Chamar o outro arquivo (Agencia)
from Agencia import ContaCorrente

# conta_duda é um objeto que pertence a classe ContaCorrente
conta_duda = ContaCorrente('Duda', '123.456.789-12', '0254', '130055519')
print('Saldo da Conta = ', conta_duda.saldo)
print('Cliente = ', conta_duda.nome)
print('CPF = ', conta_duda.cpf)

conta_duda.consultar_saldo()

conta_duda.depositar_dinheiro(10000)
conta_duda.consultar_saldo()
# conta_duda.sacar_dinheiro(1000)
# conta_duda.consultar_saldo()
conta_duda.sacar_dinheiro(7000)
conta_duda.consultar_saldo()
conta_duda.consultar_historico_transacoes()

conta_maeDuda=ContaCorrente('Maria', '123.456.789-42', '0254', '516688879')
print('Saldo da Conta = ', conta_maeDuda.saldo)
print('Cliente = ', conta_maeDuda.nome)
print('CPF = ', conta_maeDuda.cpf)
conta_duda.transferir(1000, conta_maeDuda)
conta_maeDuda.consultar_saldo()
conta_maeDuda.consultar_historico_transacoes()

help(ContaCorrente)