

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("O saldo de {} é de {}".format(self.__titular,self.__saldo))

    def deposito(self, valor):
        self.saldo += valor

    def __saque_aceito(self, valor_do_saque):
        valor_permitido = self.__saldo = self.__limite
        return valor_do_saque <= valor_permitido

    def saque(self, valor):
        if(self.__saque_aceito(valor)):
            self.__saldo -= valor
        else:
            print(f"Não foi possível sacar o valor de R${valor}, cheque seu limite!")

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular


    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def set__limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}