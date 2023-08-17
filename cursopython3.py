from time import sleep
from threading import Thread
def tarefa(tempo_espera, nome_tarefa):
    print(f'\nIniciando a terefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {nome_tarefa}')

t1= Thread(target=tarefa, args=(3, 'A'))
t2= Thread(target=tarefa, args=(2, 'B'))
t1.start()
t2.start()
t1.join()
t2.join()
print('A execução foi concluida')

#exercicio 2 abaixo.

from time import sleep
from threading import Thread
def calcular_cubo(num,tempo_espera):
    print(f'\nCubo: {num* num* num}')
    sleep(tempo_espera)
    print(f'Conclusão da função calcular_cubo')
def calcular_quadrado(num, tempo_espera):
    print(f'\nQuadrado: {num* num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_quadrado')
t1= Thread(target=calcular_quadrado, args=(5,3))
t2= Thread(target=calcular_cubo, args=(5,2))
t1.start()
t2.start()
t1.join()
t2.join()
print('A execução foi concluida!')
