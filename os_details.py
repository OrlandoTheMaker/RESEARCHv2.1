import socket
import nmap
import time
import os
import sys
import random
import pyfiglet
from colorama import Fore, Style

# Colors
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
RS = Style.RESET_ALL
R = Fore.RED
CY = Fore.CYAN
LR = Fore.LIGHTRED_EX
colors = (G, Y, B, RS, R, CY, LR)

# Symbols
info = f'{B}[{Y} I {B}]{RS}'
fail = f'{B}[{R} XX {B}]{RS}'
good = f'{B}[{G} OK {B}]{RS}'
warn = f'{B}[{LR} ! ! {B}]{RS}'
tags = f'{B}[{LR} OPTIONS {B}]{RS}'

# Banner
font = pyfiglet.figlet_format('DeTeCt_Os', font='cyberlarge')
font1 = f'{random.choice(colors)}{font}{info}Author: OrlandoTheMaker\n'
print(font1)
print(info + CY + 'OS Detector By OrlandoTheMaker\n' + RS)
print(info + CY + 'VERSION: 2.1\n' + RS)

host = input(tags + 'enter host: ')
ip = socket.gethostbyname(host)


def get_os_details(target_ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip, arguments='-O')

    if target_ip in nm.all_hosts():
        if 'osmatch' in nm[target_ip]:
            os_matches = nm[target_ip]['osmatch']
            if len(os_matches) > 0:
                os_details = os_matches[0]['osclass'][0]
                print(f"\n{good} OS details for {B}[{target_ip}]:")
                print(f"{good} Operating System :   {G}[{os_details['osfamily']}]")
                print(f"{good} Os Vendor : {G}[{os_details['vendor']}]")
                print(f"{good} OS Version :  {G}[{os_details['osgen']}]")
            else:
                print(f"{fail}No OS details found for {target_ip}")
        else:
            print(f"{fail}No OS details found for {target_ip}")
    else:
        print(f"{fail}Host {target_ip} is not available or could not be scanned")


def function4():
    go_further = input(info + 'Hit enter to continue: ')
    menu = {1: 'Return To Main Menu', 2: 'Scan A Different Website', 3: 'Quit'}

    for key, value in menu.items():
        print(key, ':', value)

    opti = int(input(f'\n{info} What Do You Want To Do? :  '))

    if opti == 1:
        os.system('clear')
        time.sleep(0.5)
        os.system('python research.py')

    elif opti == 2:
        print(info + 'Please Wait . .')
        time.sleep(0.6)
        os.system('clear')
        os.system('python os_details.py')

    elif opti == 3:
        time.sleep(2)
        os.system('python quit.py')

    else:
        print('Please Enter A Correct Option')
        time.sleep(2)
        os.execv(sys.executable, [sys.executable] + sys.argv)


# Usage example
target_ip = ip
get_os_details(target_ip)
function4()