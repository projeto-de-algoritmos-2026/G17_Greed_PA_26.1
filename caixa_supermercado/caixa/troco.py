def alg_troco(valor, moedas):
    contador = [0]*len(moedas)

    for i in range(len(moedas)):
            contador[i] = valor // moedas[i]
            valor = valor % moedas[i]

    return contador