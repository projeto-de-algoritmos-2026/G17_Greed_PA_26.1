from decimal import Decimal, ROUND_HALF_UP
def para_centavos(valor):
    return int((Decimal(str(valor)) * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

def alg_troco(valor, moedas):
    contador = [0]*len(moedas)

    for i in range(len(moedas)):
                contador[i] = valor // moedas[i]
                valor = valor % moedas[i]

    return contador