import urllib.request

try:
    webUrl = urllib.request.urlopen('http://www.pudim.com.br/')
except Exception:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')