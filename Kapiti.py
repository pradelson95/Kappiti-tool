from time import sleep
from spanlp.palabrota import *
from spanlp.domain.countries import Country

try:
    from googlesearch import search

except ImportError:
    print("no existe ese modulo")

BuscarEnInternet = input("\033[1;36m" + "[+] Ingrese algo para buscar en Internet:")

def Advertencia():
    words = ["coño",
             "coñaso", "Hijo de puta", "Maldito", "Hijo de la gran puta", "Mmg", "porno", "porn", "verga", "mmg",
             "vagina", "pene", "sexo"]

    for word in words:
        while word in BuscarEnInternet:
            print("\033[91m" + "ADVERTENCIA: NO SE ACEPTAN BUSQUEDAS EXPLICITAS O CON PALABRAS VULGARES \n")
            sleep(3)
            break


    else:
        print("\033[1;36m" + "[+] Ingresaste " + BuscarEnInternet + " para buscar en Google...\n")
        sleep(3)

        palabrota = Palabrota(censor_char="*", countries=[Country.REPUBLICA_DOMINICANA], include= ["coño",
        "coñaso", "Hijo de puta", "Maldito", "Hijo de la gran puta", "Mmg", "porno", "porn", "verga"])

        print(palabrota.censor(BuscarEnInternet))

        for busqueda in search(BuscarEnInternet, tld="co.in", num=100, stop=25, pause=2):
            print("\033[33m" + "[+]" + "\033[33m"
            + " Buscando en internet: " + BuscarEnInternet, busqueda)
            sleep(3)

        for url in BuscarEnInternet:
            palabrota = Palabrota(censor_char="*", countries=[Country.REPUBLICA_DOMINICANA, Country.MEXICO], include=["coño",
                                                                                                  "coñaso",
                                                                                                  "Hijo de puta",
                                                                                                  "Maldito",
                                                                                                  "Hijo de la gran puta",
                                                                                                  "Mmg", "porno",
                                                                                                  "porn","pene","vagina"
                                                                                                  "a la verga"])
            print(palabrota.censor(busqueda))
            break

Advertencia()

