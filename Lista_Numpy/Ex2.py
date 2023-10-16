'''Crie um programa que utilize arrays com NumPy para armazenar os dados de
temperatura média diária de uma cidade nos últimos sete dias e calcule a
temperatura média e a temperatura máxima e mínima registrada nesse período.'''

import numpy as np

temperatura=np.array([36.2,37.4,41.5,28.2,33,24,27.6,])
temp_maxima=np.max(temperatura)
temp_minima=np.min(temperatura)
print(f"A temperatura máxima foi {temp_maxima}")
print(f"A temperatura mínima foi {temp_minima}")
