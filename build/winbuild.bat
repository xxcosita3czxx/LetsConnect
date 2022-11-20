@echo off
pip install click
pip install network
pip install pyinstaller
cd ..
pyinstaller --onefile --add-data LICENSE;. --add-data README.md;. --clean -i assets/images.ico LetsConnect.py
