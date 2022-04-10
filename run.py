from settings import config
from colorama import Fore
import platform
import os

if __name__ == '__main__':

    while True:
        config.clear_screen()
        config.check_version()
        config.check_module()
        config.banner()
        config.main_list()

        commend = input(Fore.GREEN + f'''
┌──({Fore.LIGHTCYAN_EX + platform.uname()[0] + '@' + platform.uname()[1]}{Fore.GREEN})-[{Fore.LIGHTWHITE_EX + os.getcwd()}{Fore.GREEN}]
└─$ ''')

        if commend == "0":
            print(Fore.LIGHTRED_EX + "\nbye ):")
            exit()

        elif commend == "1":
            config.clear_screen()
            config.info_list()

        elif commend == "2":
            config.clear_screen()
            config.scan_list()

        elif commend == "3":
            config.clear_screen()
            config.attack_list()