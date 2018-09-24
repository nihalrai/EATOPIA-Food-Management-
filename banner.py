import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
def display():
    cprint(figlet_format('EATOPIA', font='starwars', width=5000),
           'blue', 'on_red', attrs=['bold'])
