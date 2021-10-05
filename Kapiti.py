from time import sleep
from spanlp.palabrota import *
from spanlp.domain.countries import Country
from colorama import *

urls = "\n"

print('\33[91m'"""
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    
""")

try:
    from googlesearch import search

except ImportError:
    print("no existe ese modulo")

try:

    BuscarEnInternet = input("\033[96m" + "[+] Ingrese algo para buscar en Internet>")

    words = ["coño",
             "coñaso", "Hijo de puta", "Maldito", "Hijo de la gran puta", "Mmg", "porno", "porn", "verga", "mmg",
             "vagina", "pene", "sexo"]

    for word in words:
        while word in BuscarEnInternet:
            print(Fore.LIGHTRED_EX + "ADVERTENCIA: NO SE ACEPTAN BUSQUEDAS EXPLICITAS O CON PALABRAS VULGARES \n")
            sleep(3)
            break


    else:
        print(Fore.LIGHTYELLOW_EX + "[+] Ingresaste " + BuscarEnInternet + " para buscar en Google...\n")
        sleep(3)

        palabrota = Palabrota(censor_char="*", countries=[Country.REPUBLICA_DOMINICANA], include=["coño",
                                                                                                  "coñaso",
                                                                                                  "Hijo de puta",
                                                                                                  "Maldito",
                                                                                                  "Hijo de la gran puta",
                                                                                                  "Mmg", "porno",
                                                                                                  "porn", "verga"])

        print(palabrota.censor(BuscarEnInternet))

        for busqueda in search(BuscarEnInternet, tld="co.in", num=100, stop=25, pause=2):
            print("\033[93m" + "[+]" + "\033[93m"
                  + " Buscando en internet: " + BuscarEnInternet,busqueda)
            urls = urls + busqueda + "\n"
            sleep(3)

        for url in BuscarEnInternet:
            palabrota = Palabrota(censor_char="*", countries=[Country.REPUBLICA_DOMINICANA, Country.MEXICO],
                                  include=["coño",
                                           "coñaso",
                                           "Hijo de puta",
                                           "Maldito",
                                           "Hijo de la gran puta",
                                           "Mmg", "porno",
                                           "porn", "pene", "vagina"
                                                           "a la verga"])

            print(palabrota.censor(busqueda))
            break

except (ConnectionError, KeyboardInterrupt, SystemError):
    pass

file = open("results.txt", "w")
file.write("kapiti detecto que escribiste: " + BuscarEnInternet + " para buscar en internet")
file.write(urls)
file.close()

    


























"""import platform
import socket
from tabulate import *
from colorama import *
from time import sleep

Systeminfo = [["Sistema operativo ", platform.system()], ["El procesador",platform.processor()],
              ["La arquitectura ",platform.architecture()], ["Version de sistema",platform.version()],
              ["Tipo de maquina",platform.machine()],["Node",platform.node()]]

ListSystemInfo = ["obteniendo informacion del sistema operativo",
                  "Obteniendo informacion del procesador",
                  "Obteniendo informacion de la arquitectura"
                 ,"Obteniendo la version del sistema operativo",
                  "Obtetiendo el tipo de maquina"
                  "Obteniendo la ip"]

for elemento in ListSystemInfo:
    print(Fore.LIGHTGREEN_EX + elemento)
    sleep(1)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(tabulate(ip))

print(Fore.LIGHTRED_EX + tabulate(Systeminfo))
sleep(2)"""







