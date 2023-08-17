larg=float(input('Largura da parede:'))
alt=float(input('Altura da parede:'))
ar= larg*alt
print('Sua parede tem a dimensão de {}x{} e sua aréa é de {}'.format(larg, alt, ar))
tin= ar/ 2
print('Para pintar essa parede você precisará de {}l de tinta.'.format(tin))