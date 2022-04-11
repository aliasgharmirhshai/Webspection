import os
import platform
from colorama import Fore
from time import sleep
import run

def banner():
    RED = '\033[31m'
    print(RED + "Banner\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Check Python Version 
def check_version():
    python_version = platform.python_version()

    if '3' in python_version:
        pass
    else:
        print("Please Install Python3")
        exit()

# Check Python Modules 
def check_module():
    try:
        from colorama import Fore
    except ModuleNotFoundError:
        print("Please Install colorama ( pip install colorama )")
        exit()

    try:
        import requests
    except ModuleNotFoundError:
        print("\n\tPlease Install requests ( pip install requests )\n")
        exit()

# Show List
def main_list():
    print(Fore.LIGHTYELLOW_EX + "[+] Chosse One Options\n")
    sleep(0.2)
    print(Fore.LIGHTRED_EX + "OPTIONS:\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[1] Information Gathering\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[2] Scanning\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[3] Web Attacking\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[0] EXIT\n")
    sleep(0.1)

# Information Gathering
def info_list():
    clear_screen()
    print(Fore.LIGHTBLUE_EX + "\t\tINFORMATION GATHERING\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "OPTIONS:\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[1] Information Gathering\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[0] Back\n")
    sleep(0.1)

    try:
        info_command = input(Fore.LIGHTCYAN_EX + f'''
┌──(Webspection/information-gathring/)
└─$ {Fore.LIGHTWHITE_EX}''')

        if info_command == "0":
            start()
        
    except EOFError:
        print(Fore.LIGHTRED_EX + "\nbye ):")
        exit()

# Scanning
def scan_list():
    print(Fore.LIGHTBLUE_EX + "\t\tSCANNING\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "OPTIONS:\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[1] Scanning\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[0] Back\n")
    sleep(0.1)

    try:
        scan_command = input(Fore.LIGHTCYAN_EX + f'''
┌──(Webspection/information-gathring/)
└─$ {Fore.LIGHTWHITE_EX}''')

        if scan_command == "0":
            start()
        
    except EOFError:
        print(Fore.LIGHTRED_EX + "\nbye ):")
        exit()

# Web Attacking
def attack_list():
    print(Fore.LIGHTWHITE_EX + "\t\t[3] WEB ATTACKING\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "OPTIONS:\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[3] Web Attacking\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[0] Back\n")
    sleep(0.1)

    try:
        attack_command = input(Fore.LIGHTCYAN_EX + f'''
┌──(Webspection/information-gathring/)
└─$ {Fore.LIGHTWHITE_EX}''')

        if attack_command == "0":
            start()
        
    except EOFError:
        print(Fore.LIGHTRED_EX + "\nbye ):")
        exit()


def start():
        clear_screen()
        check_version()
        check_module()
        banner()
        main_list()

        try:
            command = input(Fore.GREEN + f'''
┌──({Fore.LIGHTCYAN_EX + platform.uname()[0] + '@' + platform.uname()[1]}{Fore.GREEN})-[{Fore.LIGHTWHITE_EX + os.getcwd()}{Fore.GREEN}]
└─$ ''')

            if command == "0":
                print(Fore.LIGHTRED_EX + "\nbye ):")
                exit()

            elif command == "1":
                info_list()

            elif command == "2":
                clear_screen()
                scan_list()

            elif command == "3":
                clear_screen()
                attack_list()

        except EOFError:
            print(Fore.LIGHTRED_EX + "\nbye ):")
            exit()