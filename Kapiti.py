from time import sleep
from colorama import *
from spanlp.palabrota import *
from spanlp.domain.countries import Country

try:

    from googlesearch import search

except ImportError:
    print("no existe ese modulo")

BuscarEnInternet = input(Fore.LIGHTCYAN_EX + "[+] Buscar en Google:")
color = '\033[34m'

print(color + "[+] Ingresaste " + BuscarEnInternet + " para buscar en Google...\n")
sleep(3)

palabrota = Palabrota(censor_char="*", countries=[Country.REPUBLICA_DOMINICANA], include= ["coño",
"coñaso", "Hijo de puta", "Maldito", "Hijo de la gran puta", "Mmg", "porno", "porn"])

print(palabrota.censor(BuscarEnInternet))

for busqueda in search(BuscarEnInternet, tld="co.in", num=32, stop=10, pause=2):
      print(Fore.MAGENTA + "[*]" + Fore.LIGHTGREEN_EX
            + " Buscando en internet: " + BuscarEnInternet, busqueda)
      sleep(3)

for url in BuscarEnInternet:
        palabrota = Palabrota(censor_char="*", countries=[Country.REPUBLICA_DOMINICANA], include=["coño",
                                                                                                  "coñaso",
                                                                                                  "Hijo de puta",
                                                                                                  "Maldito",
                                                                                                  "Hijo de la gran puta",
                                                                                                  "Mmg", "porno",
                                                                                                  "porn","pene","vagina"])
        print(palabrota.censor(busqueda))
        break
