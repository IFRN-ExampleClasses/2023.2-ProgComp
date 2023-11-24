lista_A = [_ for _ in range(1,101)]

lista_B = [ [i, i**0.5] for i in lista_A if i**0.5 == int(i**0.5)]
           