#!/bin/bash

sudo apt install python3
pip install network
pip install click
pip install pyinstaller
cd ..
pyinstaller --onefile --clean --add-data LICENSE:. --add-data README.md:. -i assets/images.ico LetsConnect.py
