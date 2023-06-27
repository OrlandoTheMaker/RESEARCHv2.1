apt update && apt upgrade -y
pkg install python3 -y
pkg install git
git clone https://github.com/OrlandoTheMaker/RESEARCHv1.1.git
pip3 install -r requirements.txt
python research.py
