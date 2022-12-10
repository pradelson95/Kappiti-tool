from time import sleep
from spanlp.palabrota import Palabrota
from googlesearch import search
from colorama import Fore
from Banner import logo

try:
    Search = input("Que desea buscar?: ")
    results = int(input("Cuantos resultados desea obtener?: "))
    print(Fore.YELLOW + "Buscando", Search, "en Google..." + "\n")
    sleep(2)

    if Palabrota().contains_palabrota(Search):
        print("\033[91m! No puedes realizar busquedas explicitas")
        exit(204)

    if results < 500: print("\033[91mel limite de busquedas es meñor a 500"); exit(204)

    for url in search(query=Search, tld="com", stop=results, num=results, verify_ssl=True, lang="es"):
        print(Fore.YELLOW + "enlace: " + url)
        sleep(2)

except Exception as error:
    pass
