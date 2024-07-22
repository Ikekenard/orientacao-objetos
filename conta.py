
class Conta:

# 1)Adicionando função de inicialização
     def __init__(self,numero,titular,saldo,limite):
          print(f'construindo objeto...{self}')
          self.__numero = numero
          self.__titular = titular
          self.__saldo = saldo
          self.__limite = limite
          self.__codigo_banco = '001'

# 2) Adicionando metodos (O que está atrelado a classe e oq ela pode fazer)
# Metodos são encapsulados  
     def extrato(self):
          print(f'Saldo de:{self.__saldo} do titular:{self.__titular}')
          
     def deposita(self, valor):
          self.__saldo += valor

# Verifica se pode ou não sacar
     def __pode_sacar(self, valor_a_sacar):
          valor_disponivel_a_sacar = self.__saldo + self.__limite
          return valor_a_sacar <= valor_disponivel_a_sacar 

     def saca(self, valor):
         if(self.__pode_sacar(valor)):
             self.__saldo -= valor
         else:
             print("O valor {} passou o limite".format(valor))          
          
# 3) Encapsulamento é restringir o atributo deixando ele privado com __

     def tranfere(self, valor, destino):
          self.saca(valor)
          destino.deposita(valor)
          
# 4 Usado Getter e Setters  (property & .setter)
# Criando metodo pega_saldo (GET ou property)
#
     def get_saldo(self):
          return self.__saldo
     
     # @property
     # def saldo(self):
          # return self.__saldo
     
     def get_titular(self):
          return self.__titular
     
     # @property
     # def tituar(self):
          # return self.__titular
     
     # def get_titular(self):
          # return self.__titular
     
     @property
     def limite(self):
          return self.__limite
     
# Criando metodo para mudar/alterar (SET ou x.setter)
     @limite.setter
     def limite(self, limite):
          self.__limite = limite
     
# Deixando o método como estático 
     # @property
     @staticmethod
     def codigo_banco():
          return '001'
     
     # @property
     @staticmethod
     def codigos_bancos():
          return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

# 1) Criando contas por meio do molde da classe
conta = Conta(123, 'Ike', 55.0, 1000.0)
conta2 = Conta(524, 'Jose', 105.0, 10000.0)

# # 1) Acessando Atributos de 'conta'
# print(conta.saldo) 


# # 2) Acessando atributos de 'conta' por meio dos metodos definidos da classe

# Depositando
conta.deposita(15)
conta.extrato()

# Sacando
conta.saca(10)
conta.extrato()

# 3) Acessando atributos apos o encapsulamento
print(conta._Conta__limite)

# Transferir sem método
# valor = 10

# conta2.saca(valor)

# conta.deposita(valor)

print(conta.extrato())
conta2.extrato()
conta2.tranfere(10, conta)
conta.extrato()
conta2.extrato()

# 4) Usando Get e Set
print(conta.limite)
conta.limite = 20000.0
print(conta.limite)

print(Conta.codigos_bancos())