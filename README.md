
# LetsConnect LAN Tool 1.1

This project was created as a good idea of @IHtDzenda


## Features

- server
- client
- Possibility of using as library


## Installation

Install with pip

```bash
  git clone gitproject
  cd gitproject
  python3 setup.py bdist_wheel
(this will make .whl file in dist folder)
  pip install <dist/wheel file>
```
Install with python
```
  git clone gitproject
  cd gitproject
  python3 setup.py install
```

## Building

Building is one of the easiest ways to get the tools without installing as
library. You can build it almost on anything, just make sure there were no
errors on installing reqs (network, click).

Building windows executable (if you dont trust auto winbuild.bat)
```batch
  pip install network
  pip install click
  pip install pyinstaller
  pyinstaller --onefile --clean --add-data LICENSE;. --add-data README.md;. -i assets/images.ico LetsConnect.py
```
  Building Linux executable (if you dont trust auto linbuild.sh)
```bash
  sudo apt install python3
  pip install network
  pip install click
  pip install pyinstaller
  pyinstaller --onefile --clean --add-data LICENSE:. --add-data README.md:. -i assets/images.ico LetsConnect.py
```
## Support

For support, join my [discord](́https://discord.gg/EqqHcdRJar) or email me on kokosove18@gmail.com.


## License

MIT License

Copyright (c) 2022 cosita3cz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
