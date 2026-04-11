# Aula 05 - Medidas de Dispersão
import numpy as np
import pandas as pd

B = [5, 8, 10, 12, 15]

# variancia mede o quanto os dados se afastam da média
print(f'Variância: {np.var(B)}')
print(f'Desvio padrão: {np.std(B)}')

dados = {
    'A': [1, 22, 1, 90],
    'B': [40, 45, 47, 49],
    'C': [15, 22, 33, 4]
}

df = pd.DataFrame(dados)

print(df)
print(f'\nMáximo:\n{df.max()}')
print(f'\nMáximo por linha:\n{df.max(axis=1)}')
print(f'\nMínimo:\n{df.min()}')
print(f'\nSoma:\n{df.sum()}')
print(f'\nMédia:\n{df.mean()}')
print(f'\nVariância:\n{df.var()}')
print(f'\nDesvio padrão:\n{df.std()}')
print(f'\nDescrição geral:\n{df.describe()}')
print(f'\nDescrição coluna A:\n{df["A"].describe()}')