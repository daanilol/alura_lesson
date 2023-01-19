

class Conta: #classe Nome
    def __init__(self, numero, titular, saldo, limite): #__init__ método construtor
        self.__numero = numero #atributo
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #self vincula os argumentos com os atributos da função


    def extrato(self): #método1
        print(f"Saldo {self.__saldo} do titular {self.__titular}")


    def deposita(self, valor): #método2
        self.__saldo += valor


    def saca(self, valor):
        if valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
        else:
            print('Saldo insuficiente.')
        

    def transfere(self, valor, destino): #método4
        self.saca(valor)
        destino.deposita(valor)


    @property
    def saldo(self): #método5
        return self.__saldo


    @property
    def titular(self): #método6
        return self.__titular


    @property
    def limite(self): #método7
        return self.__limite
        

    @limite.setter
    def limite(self, limite): #método8
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
