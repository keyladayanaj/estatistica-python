# Aula 02 - Média Ponderada


import numpy as np


# cada nota tem um peso diferente (ex: prova final vale mais)
notas = [718.91, 521.33, 627.9, 610.12, 930]
pesos = [5, 2, 2, 4, 5]


# np.average calcula a média levando os pesos em conta
media_ponderada = np.average(notas, weights=pesos)
print(f'A média ponderada foi: {media_ponderada:.2f}')
