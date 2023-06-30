#!/bin/bash


apt update && apt upgrade -y
pkg install python3 -y
pkg install git
pkg install fish
pip3 install -r requirements.txt
python research.py
pkg install nmap
python research.py
