import time
import os
import sys
import random
import socket
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
font = pyfiglet.figlet_format('OmAp', font='cyberlarge')
font1 = f'{random.choice(colors)}{font}{info}Author: OrlandoTheMaker\n'
print(font1)
print(info + CY + 'A Lite Port Scanner By Orlando\n' + RS)
print(info + CY + 'Features: PORT 21 - 443\n' + RS)
print(info + CY + 'VERSION: 2.1\n' + RS)


def scan_tcp_port(target_host, target_port):
    try:
        # Create a TCP socket object
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout value of 1 second
        tcp_sock.settimeout(0.1)

        # Attempt to connect to the target host and port
        result = tcp_sock.connect_ex((target_host, target_port))

        # Check if the port is open or closed
        if result == 0:
            print(f"{info}{B}TCP Port {G}{target_port}{RS} is {G}open")
        else:
            print(f"{info}{B}TCP Port {R}{target_port}{RS} is {R}closed")

        # Close the TCP socket
        tcp_sock.close()

    except socket.error:
        print("Couldn't connect to the server")


def scan_udp_port(target_host, target_port):
    try:
        # Create a UDP socket object
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set a timeout value of 1 second
        udp_sock.settimeout(0.1)

        # Send a dummy message to the target host and port
        udp_sock.sendto(b'', (target_host, target_port))

        # Attempt to receive a response
        data, addr = udp_sock.recvfrom(1024)

        # If data is received, the port is open
        if data:
            print(f"{info}{B}UDP Port {G}{target_port}{RS} is {G}open")
        else:
            print(f"{info}{B}UDP Port {G}{target_port}{RS} is {G}closed")

        # Close the UDP socket
        udp_sock.close()

    except socket.error:
        print(f"{warn} Couldn't connect to the server")


def perform_scan(target_host, target_ports, scan_type):
    if scan_type == 'tcp':
        for port in target_ports:
            scan_tcp_port(target_host, port)
    elif scan_type == 'udp':
        for port in target_ports:
            scan_udp_port(target_host, port)
    else:
        print("Invalid scan type. Please choose 'tcp' or 'udp'.")


def function3():
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
        os.system('python omap.py')

    elif opti == 3:
        time.sleep(2)
        os.system('python quit.py')

    else:
        print('Please Enter A Correct Option')
        time.sleep(2)
        os.execv(sys.executable, [sys.executable] + sys.argv)


# Usage example
target_host = input(f"{tags} Enter Target Site: ")
print(RS)
target_port = range(19, 444)

scan_type = input("Choose the scan type ('tcp' or 'udp'): ")
perform_scan(target_host, target_port, scan_type)
function3()
