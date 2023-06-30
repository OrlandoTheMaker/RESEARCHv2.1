try:
    import time
    import os
    import sys
    from colorama import *
    import pyfiglet
    import random

except ImportError():
    print('Missing Module: ')


# Colors
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
RS = Fore.RESET
R = Fore.RED
CY = Fore.CYAN
LR = Fore.LIGHTRED_EX
colors = (G, Y, B, RS, R, CY, LR)


# Symbols
info = B+'['+Y+' I '+B+']'+RS
fail = B+'['+R+' XX '+B+']'+RS
good = B+'['+G+' OK '+B+']'+RS
warn = B+'['+LR+' ! ! '+B+']'+RS
tags = B+'['+LR+' OPTIONS '+B+']'+RS


# Banner
font = pyfiglet.figlet_format('RESEARCH', font='rowancap')
font1 = (random.choice(colors)+font+info+'Author: OrlandoTheMaker')
print(font1)


def text_banner():
    messg = '' \
          f'{info}{CY} NAME::>>{RS}       JEREMIAH ABDULSALAM\n' \
          f'{info}{CY} AKA::>>{RS}        Orlando The Maker\n' \
          f'{info}{CY} Github::>>{RS}     https://www.github.com/OrlandoTheMaker\n' \
          f'{info}{CY} facebook::>>{RS}   https://web.facebook.com/profile.php?id=100093388869888\n' \
          f'{info}{CY} twitter::>>{RS}    https://twitter.com/Orlando13140\n'\
          f'{info}{CY} VERSON::>>{RS}     1.1\n'
    print(messg)
    time.sleep(2)


text_banner()

menu = {1: 'SCRAPE ALL LINKS ON A SITE',
           2: 'SCRAPE ALL EMAILS FROM WEBPAGE',
        3: 'EXTRACT DUPLICATE EMAILS FROM A FILE',
        4: 'SCAN OPEN PORTS',
        5: 'GET OPERATING SYSTEM DETAILS',
        6: 'RESTART THE TOOL',
        7: 'QUIT'
        }


print(good + 'Select An Option From Below \n')
for key, value in menu.items():
    print(Y, key, tags, Y, value, RS)


print('\n')
enter = int(input("ENTER OPTION: "))


# loop over the 'enter' option
if enter == 1:
    print(info + 'Please wait . . .')
    time.sleep(3)
    os.system('clear')
    os.system('cls')
    os.system('python links.py')

elif enter == 2:
    print(info + 'Please wait . . .')
    time.sleep(3)
    os.system('clear')
    os.system('cls')
    os.system('python emails.py')

elif enter == 3:
    print(info + 'Please wait . . .')
    time.sleep(3)
    os.system('clear')
    os.system('cls')
    os.system('python email_validator.py')

elif enter == 4:
    print(info + 'Please wait . . .')
    time.sleep(3)
    os.system('clear')
    os.system('cls')
    os.system('python omap.py')
    
elif enter == 5:
    print(info + 'Please wait . . .')
    time.sleep(3)
    os.system('clear')
    os.system('cls')
    os.system('python os_details.py')

elif enter == 6:
    print(info + 'Please wait . . .')
    time.sleep(3)
    os.system('clear')
    os.system('cls')
    os.system('python research.py')

elif enter == 7:
    print(info + 'Please wait . . .')
    time.sleep(3)
    os.system('clear')
    os.system('cls')
    print(font1)
    text_banner()
    print('\nGOOD BYE AND DO NOT FORGET TO FOLLOW ME ON GITHUB ')
    sys.exit()
