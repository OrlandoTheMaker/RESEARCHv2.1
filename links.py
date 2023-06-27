import requests
import time
import os
import sys
import csv
from bs4 import BeautifulSoup
from colorama import Fore

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

website = input(CY + 'Type Website Url: ')

# make a GET request to the website
r_get = requests.get('https://' + website)
status_code = r_get.status_code

links = []


def scrape_website(url):
    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(r_get.content, "html.parser")

    # find all the links on the website
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            links.append(href)

    return links, status_code


def save_to_csv(links):
    with open('links.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([f'     {info}         Source URL:  ', links])  # Add header indicating the source URL
        for j in links:
            writer.writerow([j])


def net_stat():
    try:
        s_c = status_code
        if status_code != 200:
            for i in range(0, 5):
                time.sleep(2)
                print(fail + 'Target Is Unreachable! ! !')
        else:
            print('')
            print(info + 'Connection_Status: Connection Is Good:')
            print(good + 'Status-Code: ', status_code)
            print('\n' * 2)
    except KeyboardInterrupt as interrupt:
        print(interrupt)
    except ConnectionError as connerr:
        print(fail + 'There has been a network error\nPlease check your internet and try again')
        print(connerr)
    except requests.exceptions.ConnectionError:
        print(fail, ' There has been a connection error')


def function1():
    go_further = input(info + 'Hit enter to continue: ')
    print('\n')
    menu = {1: 'Get All Links', 2: 'quit', 3: 'Scan A New Site', 4: 'Restart The Tool'}

    for key, value in menu.items():
        print(key, ':', value)

    opt = int(input(f'\n{info} What Do You Want To Do? :  '))

    if opt == 1:
        msg = info + 'Data is being collected. . .\n' + info + \
                     'type "cat links.csv" when completed to view the contents'

        for i in msg:
            time.sleep(0.2)
            print(i, end='')
        print('\n')
        scrape_website(website)
        save_to_csv(links)
    elif opt == 2:
        sys.exit()
    elif opt == 3:
        time.sleep(2)
        os.system('python links.py')
    elif opt == 4:
        os.system('python research.py')
    else:
        print('Please Enter A Correct Option')
        time.sleep(2)
        os.execv(sys.executable, [sys.executable] + sys.argv)


# create an empty set to store visited links
visited_links = set()

net_stat()
function1()

while True:
    # scrape the current website
    links, status_code = scrape_website(website)

    # save the links to CSV
    save_to_csv(links)

    # add the current website to visited links
    visited_links.add(website)

    # find a new unvisited link from the scraped links
    new_link = None
    for link in links:
        if link not in visited_links:
            new_link = link
            break

    if new_link is None:
        # no unvisited links found, exit the loop
        break

    # set the new link as the current URL for the next iteration
    website = new_link
