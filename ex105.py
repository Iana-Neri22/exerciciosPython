def notas(*notas, sit='False'):
    r= dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['media'] = sum(notas) / len(notas)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'

    return r

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)