import os
import sys
from colorama import Fore, Style
from time import sleep
from modules.info import robots, dns_lookup

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
    

# Show List
def help_list():
    clear_screen()
    banner()
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f"""
    Developer : AliasgharMirshahi
    Version : 0.1.0
    Github : https://github.com/aliasgharmirhshai

    usage: Webspection [--help] [--dns] [-rb] 

    Examples:
        {Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} python3 Webspection.py -rb : Find robots.txt File
        {Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} python3 Webspection.py --dns -Mx : Find MX Dns ( Mail Server )
        {Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} python3 Webspection.py --dns -Ns : Name Server Lookup ( Dns )

""")

# Project Handelr
def start():

    try:
        if sys.argv[1] == '--help':
            help_list()

        elif sys.argv[1] == '-rb':
            robots.__start__()

        elif sys.argv[1] == '--dns':
            dns_lookup.dns_handler()
        
        else:
            print(Fore.LIGHTRED_EX + f"Command Not Found\n")
    
    except IndexError:
        clear_screen()
        banner()
        print(Style.BRIGHT + "\tPlease Choose One Option\n")
    
# Run 
if __name__ == '__main__':
    
    start()