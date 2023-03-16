# DesktopClicksStats
Python program to collect statistics about clicks on desktop

## Requirements
* Windows
* Python 3.9+
* `pywin32` - `pip install pywin32`
* `pynput` - `pip install pynput`
* (For render.py) `PIL` - `pip install Pillow`

## Installation
* Download repository zip
* Extract zip files to new folder

## Using

* At start, click at your desktop and then press Enter key.
* To show your statistics graphically, put some image to project folder and name it `desktop.png` or don`t put that image to create transparent render, and then launch `render.py` file. This will create render.png file with resut render
* Adding to startup:
  - Press Win+R and type there `shell:startup` and then press Enter.
  - Create new file with `.bat` extinsion in some folder and then create link to `Startup` folder that you opened in step above.
  - Make batch script change current folder to project folder and then execute command `pythonw main.py` (Example script in `startup_example.bat`)
  - After your computer starts and console window opened, click at your desktop and then press Enter key. Now you can close console window.
