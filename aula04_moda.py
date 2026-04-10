# Aula 04 - Moda
import statistics

a = [11, 2, 2, 9, 7]
b = [4, 4, 19]
c = [3, 3, 1, 9, 9]  # amodal - dois valores mais frequentes

# mode retorna o valor que mais se repete
print(f'Moda de a: {statistics.mode(a)}')
print(f'Moda de b: {statistics.mode(b)}')

# multimode retorna todos os valores mais frequentes
print(f'Moda de c: {statistics.multimode(c)}')
