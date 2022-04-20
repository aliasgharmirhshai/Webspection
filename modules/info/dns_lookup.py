import dns.resolver
from colorama import Fore, Style


def mx_rec():   
    try:
        # MX ( Find Mail Server )
        print(Fore.LIGHTBLUE_EX + "\nPlease Enter the address Without ( http:// and https:// )")
        url = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Enter Url :> ")
        
        answers = dns.resolver.resolve(url, 'MX')
        for rdata in answers:
            print(Fore.LIGHTWHITE_EX + "[+] " + Fore.LIGHTGREEN_EX + 'Host', rdata.exchange, 'has preference', rdata.preference)

    
    except dns.resolver.NXDOMAIN:
        print(Fore.LIGHTRED_EX + "\n[-] Something Error Please Check Internet and Please Enter the address Without ( http:// and https:// )\n")
    except dns.resolver.NoAnswer:
        print(Fore.LIGHTRED_EX + '\n[-] Please Enter Url\n')
    except:
        print(Fore.LIGHTRED_EX + "By |:")

