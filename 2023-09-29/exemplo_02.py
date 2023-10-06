x = int(input('Informe um valor inteiro positivo: '))

if x > 0:
    i = 0
    while i <= x:
        if i % 2 == 0:
            print(f'{i} é PAR...')
        else:
            print(f'{i} é ÍMPAR...')
        i += 1