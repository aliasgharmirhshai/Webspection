import os
from colorama import Fore
from time import sleep

def banner():
    print("Banner\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_version():
    pass

def check_module():
    pass

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

def info_list():
    print(Fore.LIGHTBLUE_EX + "\t\tINFORMATION GATHERING\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "OPTIONS:\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[1] Information Gathering\n")
    sleep(0.1)
    input()

def scan_list():
    print(Fore.LIGHTBLUE_EX + "\t\tSCANNING\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "OPTIONS:\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[2] Scanning\n")
    sleep(0.1)

def attack_list():
    print(Fore.LIGHTWHITE_EX + "\t\t[3] WEB ATTACKING\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "OPTIONS:\n")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX + "\t[3] Web Attacking\n")
    sleep(0.1)

