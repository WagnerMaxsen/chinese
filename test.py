import urllib
import requests


"""
1. como ler o dado de entrada do programa, que é um símbolo, e deve ser convertido para utf8
"""


# comentario em codigo pode ser com uso de #
"""ou pode ser com 3 aspas para abrir
e 3 aspas fechando o bloco
"""
BLA = "可以"
# O ATALHO para setar um breakpoint é control, shift, b


# res = requests.get(
#    "https://www.purpleculture.net/dictionary-details/?word={0}".format(BLA)
# )

res = urllib.request.urlopen(
    "https://www.purpleculture.net/dictionary-details/?word={0}".format(BLA)
)


for lines in u2.readlines():
    print(lines)

temp = ""
for i in res.text.split(" "):
    if "possible" in i:
        import pdb

        pdb.set_trace()  # breakpoint 280c4dcb //


"""
outra forma de concatenar string: xablau = "dsadasdas" + BLA
"""


"""
576116952820-25tuifs97pfppqdiqrv044pkn9bf7s79.apps.googleusercontent.com
"""

"""
Igh3_KQkCktX8lxL0Wxq3Ybh
"""

# pip3 freeze  é para listar as libs instaladas pelo python3s
