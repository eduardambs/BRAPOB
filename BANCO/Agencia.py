from datetime import datetime
import pytz
# Criação da classe ContaCorrente
class ContaCorrente:
    '''
        A classe ContaCorrente simula o funcionamento de uma Conta Conrrente Real
    '''
# Construtor da classe ContaCorrente
# Possui três atributos
    def __init__(self, nome, cpf, agencia, num_conta):
# Atributos da classe
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
    def consultar_saldo(self):
        print('Seu saldo atual = R${:,.2f}'.format(self.saldo))

# Método para depositar valores
    def depositar_dinheiro(self, valor):
        self.saldo += valor
      #  self.sald = self.saldo + valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
    # acrescentar um parenteses para transformar duas informações em apenas uma informação (tupla)
    # pega uma determinada informação para incluir na lista, apenas uma

# Método para sacar
    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print('Você não tem saldo suficiente para sacar este valor!')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def limite_conta(self):
        self.limite = -1000
        return self.limite

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def consultar_historico_transacoes(self):
        print('Histórico de transações')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


