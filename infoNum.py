#Tool created by DW Dariel(Gustavo Hernandez)
#Tool created to study python libraries
import requests
from getpass import _raw_input
from colorama import Fore, init
init()

api = '510f8c00e437e5c107b8629d2fe5ca20'

print("""
 _        __       _   _                 
(_)_ __  / _| ___ | \ | |_   _ _ __ ___  
| | '_ \| |_ / _ \|  \| | | | | '_ ` _ \ 
| | | | |  _| (_) | |\  | |_| | | | | | |
|_|_| |_|_|  \___/|_| \_|\__,_|_| |_| |_|
                                         
                                                                                             


""")

print(Fore.GREEN+"\nScript hecho por DW Dariel")

numero = int(_raw_input("\nIngrese el numero: "))

info = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api, numero))

for key, valor in info.json().items():
    print("\n%s: %s" % (key, valor))
