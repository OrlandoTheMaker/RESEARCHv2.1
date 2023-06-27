import requests
from bs4 import BeautifulSoup
import csv
import re
from colorama import Fore
import os
import sys
import time

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
info = B+'['+G+' I '+B+']'+RS
fail = B+'['+R+' XX '+B+']'+RS
good = B+'['+G+' OK '+B+']'+RS
warn = B+'['+G+' ! ! '+B+']'+RS


def scrape_website(urls):
    # make a GET request to the website
    response = requests.get(urls)

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # find all the email addresses on the website
    emails = re.findall(r"[a-zA-Z0-9\.\-\_i]+@[a-zA-Z0-9\w.]+", str(soup))

    return emails


def save_to_csv(emails):
    with open('emails.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for email in emails:
            print(B + email + RS)
            writer.writerow([email])
    time.sleep(0.7)
    print(good + 'Completed! ' + good + 'Results saved to "emails.csv" file\n' + RS)


def function2():
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
        os.system('python emails.py')

    elif opti == 3:
        time.sleep(2)
        os.system('python quit.py')

    else:
        print('Please Enter A Correct Option')
        time.sleep(2)
        os.execv(sys.executable, [sys.executable] + sys.argv)


url = input(CY + 'Enter the site here: ')
urls = 'https://' + url
emails = scrape_website(urls)
save_to_csv(emails)
function2()

