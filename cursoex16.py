'''from random import choice

n1= str(input('Primeiro aluno:'))
n2= str(input('Segundo aluno:'))
n3= str(input('Terceiro aluno:'))
n4= str(input('Quarto aluno:'))

lista= [n1,n2,n3,n4]
escolhido= choice(lista)
print('O aluno escolhido da lista foi {}'.format(escolhido))

#ex02
from random import shuffle

n1= str(input('Primeiro aluno:'))
n2= str(input('Segundo aluno:'))
n3= str(input('Terceiro aluno:'))
n4= str(input('Quarto aluno:'))

lista= [n1, n2, n3, n4]
shuffle(lista)
print('A ordem da apresentação será')
print(lista)'''

#ex3
'''import pygame
pygame.init()
pygame.mixer.music.load('ex16.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

import pygame

pygame.init()
pygame.mixer.music.load('ex16.mp3')
pygame.mixer.music.play()

# Loop de eventos
while pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.mixer.music.stop()



