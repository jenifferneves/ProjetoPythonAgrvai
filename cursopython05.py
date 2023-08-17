from sklearn.datasets import load_digits
digitos= load_digits()

print('Shape dos dados de imagens: {}'.format(digitos.data.shape))
print('Shape dos dados rotulados: {}'.format(digitos.target.shape))
