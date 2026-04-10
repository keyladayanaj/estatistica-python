# Aula 01 - Média Aritmética


def calcular_media(vetor):
    return sum(vetor) / len(vetor)


# Exemplo 1: notas do aluno
notas = [7, 8, 6, 10]
print(f'A média do aluno foi: {calcular_media(notas)}')


# Exemplo 2: endividamento de empresas
endividamento = [25, 51, 76, 41, 55, 13]
print(f'A média do endividamento das empresas foi: {calcular_media(endividamento)}%')


# Exemplo 3: vendas (atenção: valor 300 é um outlier)
vendas = [10, 17, 13, 300]
print(f'A média das vendas: {calcular_media(vendas)}')