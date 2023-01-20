import requests
from colorama import Fore, Style
from ..lib import get_target

def __start__():
    try:
        host = get_target(command_range=2, url_range=3)

        if 'https://' in host:
            pass
        else:
            host = f'https://{host}'

        response = requests.get(f'{host}/robots.txt').text
        print(Fore.LIGHTWHITE_EX + response)

        save_file = input(Fore.LIGHTGREEN_EX + "Do You Want The Output To be Saved? (y or n) :> ")

        if save_file == 'y':
            with open("robots.txt", "w") as robot_file:
                robot_file.write(response)
                print(Fore.LIGHTGREEN_EX + "\n[+] Saved File\n")
        else:
            pass

    except requests.exceptions.ConnectionError:
        print(Fore.LIGHTRED_EX + '\n[-] Something Error Please Check Internet and Please Enter the address Without ( http:// and https:// )\n')
    except requests.exceptions.InvalidURL:
        print(Fore.LIGHTRED_EX + '\n[-] Please Enter Url\n')
    except:
        print(Fore.LIGHTRED_EX + "By |:")