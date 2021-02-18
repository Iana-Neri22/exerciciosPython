retaUm = float(input('Digite o valor da reta 1 : '))
retaDois = float(input('Digite o valor da reta 2: '))
retaTres = float(input('Digite o valor da reta 3: '))
isFormaTriangulo = retaUm < retaDois + retaTres and retaDois < retaUm + retaTres and retaTres < retaUm + retaDois

if isFormaTriangulo:
    if retaUm == retaDois == retaTres:
        print('Forma um triângulo equilátero.')
    elif retaUm == retaDois or retaUm == retaTres:
        print('Forma um triângulo isósceles.')
    else:
        print('Forma um triângulo escaleno')
else:
    print('Não forma um triângulo')
