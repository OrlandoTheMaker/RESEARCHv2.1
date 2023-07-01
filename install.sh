#!/bin/bash
apt update && apt upgrade -y
pkg install python3 -y
pkg install git
pkg install fish
pkg install pip
pip3 install -r requirements.txt
pkg install nmap
pip install colorama
pip install pyfiglet
pip install bs4
pip install requests
pip install python-nmap
python research.py
