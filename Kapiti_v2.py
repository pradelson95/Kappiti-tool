from time import sleep
from googlesearch import search
from colorama import Fore

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
    Search = input("Que desea buscar?: ")
    results = int(input("Cuantos resultados desea obtener?: "))
    print(Fore.YELLOW + "Buscando", Search, "en Google..." + "\n")
    sleep(2)

    for url in search(query=Search, tld="com", stop=results, num=results, verify_ssl=True, lang="es"):
        print(Fore.YELLOW + "enlace: " + url)
        sleep(2)

except Exception as error:
    pass
