continua = 'S'
lista = []

while continua == 's' or continua == 'S':
    n = float(input('Digite um número: '))
    lista.append(n)
    continua = input('Deseja continuar? (s/n): ')

print(lista)