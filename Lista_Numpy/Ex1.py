'''Usando arrays com numpy faça média das notas de uma pessoa estudante.'''

import numpy as np

notas=np.array([10,8.5,9])
media=np.mean(notas)
print(f"A média das notas é igual a {media:.2f}")
