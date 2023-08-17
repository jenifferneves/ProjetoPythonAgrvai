#ex1

co=float(input('Qual o valor do cateto oposto:'))
ca=float(input('Qual o valor do cateto adjacente:'))
hi=(co**2+ ca**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#ex2

from math import hypot 
co=float(input('Qual o valor do cateto oposto:'))
ca=float(input('Qual o valor do cateto adjacente:'))
hi= hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#ex3

import math
ag=float(input('Digite o valor do ângulo:'))
seno= math.sin(math.radians(ag))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ag, seno))
cosseno= math.cos(math.radians(ag))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ag, cosseno))
tan= math.tan(math.radians(ag))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ag, tan))

#ex4

from math import radians, sin, cos, tan
ag=float(input('Digite o valor do ângulo:'))
seno= sin(radians(ag))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ag, seno))
cosseno= cos(radians(ag))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ag, cosseno))
tang= tan(radians(ag))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ag, tang))
