class Cliente: 
     def __init__(self,nome):
          self.__nome = nome

# Usando get como propriedade ja existente no método da classe
     @property
     def nome(self):
          print(f'chamando o @property nome()')
          return self.__nome.title()

# Usando uma set como um set já existente da própria classe
     @nome.setter
     def nome(self, nome):
          print(f'chamando o setter nome()')
          self.__nome = nome
           
     
cliente = Cliente('ike')
print(cliente.nome)

cliente.nome = 'caroline'
print(cliente.nome)