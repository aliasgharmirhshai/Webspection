import dns.resolver
from colorama import Fore, Style
import sys

# Get Target Url
try:
    if sys.argv[3] == '--host':
        host = sys.argv[4]
    else:
        print('Command Not Found\n')
except IndexError:
    print('Pleases Enter url')

# Dns Tools Handler
def dns_handler():

    if sys.argv[2] == '-Mx':
        mx_rec()

    elif sys.argv[2] == "-Ns":
        ns_lookup()

    else:
        print(Fore.LIGHTRED_EX + f"Command Not Found\n")


# MX ( Find Mail Server )
def mx_rec():   
        try:            
            answers = dns.resolver.resolve(host, 'MX')
            for rdata in answers:
                print(Fore.LIGHTWHITE_EX + "[+]" + Fore.LIGHTGREEN_EX + 'Host', rdata.exchange, 'has preference', rdata.preference)
        
        except dns.resolver.NXDOMAIN:
            print(Fore.LIGHTRED_EX + "\n[-] Something Error Please Check Internet and Please Enter the address Without ( http:// and https:// )\n")
        except dns.resolver.NoAnswer:
            print(Fore.LIGHTRED_EX + '\n[-] Please Enter Url\n')
        except:
            print(Fore.LIGHTRED_EX + "By |:")

# Name Server
def ns_lookup():
    try:
        answers = dns.resolver.query(host,'NS')
        for server in answers:
            res = server.target
            print(f'{Fore.LIGHTWHITE_EX}[+]{Fore.LIGHTGREEN_EX} {res}')
    
    except dns.resolver.NXDOMAIN:
        print(Fore.LIGHTRED_EX + "\n[-] Something Error Please Check Internet and Please Enter the address Without ( http:// and https:// )\n")
    except dns.resolver.NoAnswer:
        print(Fore.LIGHTRED_EX + '\n[-] Please Enter Url\n')



