def aumentar(valor, pct, formatar):
    porcentagem = valor * (pct / 100)

    if formatar:
        return moeda(valor + porcentagem)
    else:
        return valor + porcentagem


def diminuir(valor, pct, formatar):
    porcentagem = valor * (pct/100)

    if formatar:
        return moeda(valor - porcentagem)
    else:
        return valor - porcentagem


def dobro(valor, formatar):
    if formatar:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor, formatar):
    resultado = valor / 2
    if formatar:
        formatado = moeda(resultado)
        return formatado
    else:
        return resultado

def moeda(moeda):
    return f'R${moeda:.2f}'.replace('.', ',')


def resumo(valor, aumento, reducao):

    print(f'Preço analisado: {moeda(valor)}')
    print(f'Dobro do preço: {dobro(valor, True)}')
    print(f'Metade do preço: {metade(valor, True)}')
    print(f'{aumento}% de aumento: {aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: {diminuir(valor, reducao, True)}')


