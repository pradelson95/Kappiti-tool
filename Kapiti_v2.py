from time import sleep
from googlesearch import search
from colorama import Fore
from Banner import logo

try:
    Search = input("Que desea buscar?: ")
    results = int(input("Cuantos resultados desea obtener?: "))
    print(Fore.YELLOW + "Buscando", Search, "en Google..." + "\n")
    sleep(2)

    for url in search(query=Search, tld="com", stop=results, num=results, verify_ssl=True, lang="es"):
        print(Fore.YELLOW + "enlace: " + url)
        sleep(2)

except Exception as error:
    pass
