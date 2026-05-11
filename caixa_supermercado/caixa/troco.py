def alg_troco(valor, moedas):
    contador = [0]*len(moedas)

    for i in range(len(moedas)):
            if valor%moedas!= 0:
                contador[i] = valor // moedas[i]
                valor = valor % moedas[i]

    return contador