# 4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
# métodos “depositar” e “sacar” para manipular o saldo

class ContaBancaria:

    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
        self.depositar = ()
        self.sacar = ()

    def depositar(self):
        self.depositar = (self.saldo + self.depositar)
        return self.depositar

    def sacar(self):
        self.sacar = (self.saldo - self.sacar)
        return self.sacar

    





