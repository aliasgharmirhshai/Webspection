import sys
from time import sleep
import os
from colorama import Fore, Style

BLUE = '\033[34m'


def banner():
    sleep(0.1)
    print(Style.BRIGHT + BLUE +"""\t\n
    ░██╗░░░░░░░██╗███████╗██████╗░░██████╗██████╗░███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗  
    ░██║░░██╗░░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║     
    ░╚██╗████╗██╔╝█████╗░░██████╦╝╚█████╗░██████╔╝█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║       
    ░░████╔═████║░██╔══╝░░██╔══██╗░╚═══██╗██╔═══╝░██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
    ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██████╔╝██║░░░░░███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
    ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝\n
            
    \tYou Can Enter ( python3 Webspection.py --help ) And See Options\n
""")
    sleep(0.1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Get Target Url
def get_target(command_range, url_range):
    try:
        if sys.argv[command_range] == '--host':
            host = sys.argv[url_range]
        else:
            print('Command Not Found\n')
    except IndexError:
        print('Pleases Enter url')

    return host

def troubleshooting():
    
    return "coming Soon.."