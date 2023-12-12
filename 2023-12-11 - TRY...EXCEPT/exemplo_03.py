import sys

while True:
    try:
        x = int(input('\nInforme um valor inteiro:'))
    except ValueError:
        print(f'ERRO...O Valor informado não é um inteiro válido.')
        continue
    except KeyboardInterrupt:
        print(f'AVISO...Foi pressionado CTRL+C. Saindo do programa.')
        sys.exit()
    except:
        print(f'ERRO...{sys.exc_info()[0]}')
        sys.exit()
    else:
        raiz = x ** 0.5
        break

print('Continua o programa...')