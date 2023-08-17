'''class pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender


p1 = pessoa('Maria', 'rua 01234')
p2 = pessoa('João', 'rua 56789')
print(f'Nome: {p1.get_nome()}, Endereço: {p1.get_ender()}')
print(f'Nome: {p2.get_nome()}, Endereço: {p2.get_ender()}')'''

'''class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base * 12) + self.bonus

class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario

    def salario_total(self):
        return self.salario_agregado.salario_anual()

def main():
    salario = Salario(10000, 700)
    emp = Empregado('Musashi', 46, salario)
    print(emp.salario_total())

if __name__ == '__main__':
    main()'''

'''from datetime import date
class Pessoa:
    def __init__(self, nome, idade):

        self.nome= nome
        self.idade= idade

    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    
    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18
    
pessoa1= Pessoa('maria', 26)
pessoa2= Pessoa.apartirAnoNascimento('ana', 2006)

print(pessoa1.idade)
print(pessoa2.idade)
print(Pessoa.ehMaiorIdade(17))'''

'''from datetime import date

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)

    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18

# Criando os objetos fora da classe
pessoa1 = Pessoa('maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('ana', 2006)

print(pessoa1.idade)
print(pessoa2.idade)
print(Pessoa.ehMaiorIdade(17))'''

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

def main():
    c1 = Conta(1,1,"Joao",1000) # Objeto sendo instanciado
    print (f"Nome do titular da conta: {c1.nomeTitular}")
    print (f"Número da conta: {c1.numero}")
    print (f"CPF do titular da conta: {c1.cpf}")
    print (f"Saldo da conta: {c1.saldo}")
    

# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script

if __name__ == "__main__": 
    main()


    



    