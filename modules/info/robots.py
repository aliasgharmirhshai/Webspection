import requests
from colorama import Fore, Style


def __start__():
    try:
        url = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Enter Url :> ")

        if 'http://' in url:
            pass
        else:
            url = f'http://{url}'

        response = requests.get(f'{url}/robots.txt').text
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