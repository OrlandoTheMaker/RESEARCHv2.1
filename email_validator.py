from collections import Counter
import time
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
info = B+'['+Y+' INFO '+B+']'+RS
fail = B+'['+R+' FAIL '+B+']'+RS
good = B+'['+G+' OK '+B+']'+RS
warn = B+'['+LR+' WARNNING '+B+']'+RS
tags = B+'['+LR+' OPTIONS '+B+']'+RS


def validator_banner():
    messg = f'{info}           This email validator was written by\n' \
          f'{info}        NAME::>>    JEREMIAH ABDULSALAM\n' \
          f'{info}        AKA::>>    Orlando The Maker\n' \
          f'{info}        Github::>>    https://www.github.com/OrlandoTheMaker\n' \
          f'{info}        VERSON::>>    1.1\n'
    print(messg)
    time.sleep(2)


def find_duplicates(emails):
    email_counts = Counter(emails)
    duplicates = [email for email, count in email_counts.items() if count > 1]
    return duplicates


def remove_duplicates(emails):
    email_counts = Counter(emails)
    unique_emails = [email for email, count in email_counts.items() if count == 1]
    return unique_emails


validator_banner()
msg = f'{info} Make sure to enter the exact file path without quotes'
print('\n'+msg+'\n')
# Example file path
file_path = input(f'{good} Enter file path here:  ')

# Read the file and split it into a list of emails
with open(file_path, 'r') as file:
    email_list = file.read().splitlines()

# Find and print the duplicate emails
duplicates = find_duplicates(email_list)
for email in duplicates:
    time.sleep(0.2)
    print(info, G, 'Duplicate Emails: ', R, email)

# Remove the duplicate emails
email_list = remove_duplicates(email_list)

# Print the updated list without duplicates
for email in email_list:
    time.sleep(0.2)
    print(info, G, 'Updated Email_List: ', G, email)

