import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

print(Fore.CYAN + """                             _     _     _           _ _ _                       _       _   
  __ _ _ __   __ _ _ __ ___| |__ (_)___| |_    __ _| | (_) ___  ___    ___  ___(_)_ __ | |_ 
 / _` | '_ \ / _` | '__/ __| '_ \| / __| __|  / _` | | | |/ _ \/ __|  / _ \/ __| | '_ \| __|
| (_| | | | | (_| | | | (__| | | | \__ \ |_  | (_| | | | |  __/\__ \ | (_) \__ \ | | | | |_ 
 \__,_|_| |_|\__,_|_|  \___|_| |_|_|___/\__|  \__,_|_|_|_|\___||___/  \___/|___/_|_| |_|\__|
                                                                                            """)
print("")
print("")
print("LIVING THE DARK SERVING THE LIGHT")

print("")
print("")

x = input('Request URL ( INSPECT ELEMENT ): ')
print("")
print("")

print('Launching.....')
print('')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('Report sent')

    time.sleep(10)


input()
