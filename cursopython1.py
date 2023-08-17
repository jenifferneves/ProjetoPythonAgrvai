class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome= nome
        self.velocidade_max= velocidade_max
        self.quilometro_litro= quilometro_litro

    def capacidade_assentos(self, capacidade):
        print(f'Acapacidade maxima de assentos do veiculo {self.nome} é {capacidade}')

    def toStr(self):
        print(f'nome={self.nome}')
        print(f'velocidade_max= {self.velocidade_max}')
        print(f'quilometros percorridos por litro= {self.quilometro_litro}')

class Onibus(Veiculo):
   def capacidade_assentos(self, capacidade=70):
       return super().capacidade_assentos(capacidade=70)
   
onibus_escolar= Onibus('Scania', 120, 8)
onibus_escolar.toStr()
onibus_escolar.capacidade_assentos()


veiculos= ['aviao','carro','navio','onibus']

f_maiuscula= lambda x: str.upper(x)

nomes_maiusculos= list(map(f_maiuscula, veiculos))

print(f'nomes maiusculos= {nomes_maiusculos}')

lista= [0,1,1,2,3,5,8,13,21,34]

fTesteParidade= lambda x: x % 2 == 0

pares= list(filter(fTesteParidade, lista))

print(f'lista de números pares = {pares}')

lista_numeros= [9.56783, 7.57568, 3.00914, 6.2321]
lista_precisao= [2,2,3,3]
arrendondamento= lambda x,y: round(x,y)

resultado= list(map(arrendondamento, lista_numeros, lista_precisao))
print(resultado)

from functools import reduce
f_soma= lambda x,y: x+y

numeros= [1,2,3,4,5,6,7,8,9,10]
resultado= reduce(f_soma, numeros)
print(resultado)


