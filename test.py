# 1 - Cria Conta
def cria_conta(numero,titular,saldo,limite):
     conta = {'numero': numero, 'titular':titular, 'saldo':saldo, 'limite': limite}
     return conta

# 2 - Depostia 
def deposita(conta, valor):
     conta['saldo'] += valor
     
# 3 - Saca 
def saca(conta,valor):
     conta['saldo'] -= valor
     
# 4 - Checa saldo
def extrato(conta):
    print("Seu saldo é de {}".format(conta["saldo"]))
    
    

     
# Rodando as funções
conta = cria_conta(123, 'ike', 15.0, 1000)
print(conta)

# Deposito
deposita(conta,15.0)
extrato(conta)

# Saque
saca(conta,10)
extrato(conta)
