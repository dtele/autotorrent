# AutoTorrent
AutoTorrent is a command-line tool that scrapes results and their magnets from 1337x search.

![image](https://user-images.githubusercontent.com/72906211/177021093-24287ee2-b322-48e1-8d87-f008666c64bf.png)

## Installation

Do any of the following:

- Download latest release from [releases](https://github.com/dtele/autotorrent/releases)
- Build it yourself:
    1. download compatible [chromedriver](https://chromedriver.chromium.org/downloads)
    2. `pip install selenium`
    3. `pyinstaller /path/to/main.py --onefile --add-binary "/path/to/chromedriver.exe;./driver" -n "tdl"`

Split Tunnelling can be set-up in VPN settings by including chrome.exe through VPN Tunnel.

## Usage
```
tdl [-h] search_term rows
```
- search_term: term to search
- rows: desired number of results
