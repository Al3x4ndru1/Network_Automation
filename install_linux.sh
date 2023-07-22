#!/bin/bash
echo 'Initializing...'
sudo apt -y install python3 python3.10-venv figlet >/dev/null 2>&1

figlet "Installing the requirements"

sudo apt update
sudo apt upgrade -y
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

figlet "Cleaning"

sudo 777 clean.sh
sudo ./clean.sh

python3 main.py
