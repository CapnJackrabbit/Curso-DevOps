numero = int(input("Digite um numero para ver a sua tabuada: "))
for cont in range (11):
    if cont == 0:
        pass
    else:
        print ("{} X {} = {}".format(numero, cont, numero * cont))
