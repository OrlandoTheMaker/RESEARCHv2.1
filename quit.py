import sys
import colorama
import time
from colorama import *
import os

YELLOW = Fore.YELLOW
RESET = Fore.RESET
warn = YELLOW+'[ WARNNING ]'+RESET
print('\n'*2)

ask = input(warn+' Are You Sure You Want To Quit? ! y/n    ')

if ask == 'y':
    sys.exit(0)

elif ask == 'n':
    time.sleep(2)
    os.system('python research.py')

else:
    print(warn+' kindly Select An Option')
    os.system('python quit.py')

