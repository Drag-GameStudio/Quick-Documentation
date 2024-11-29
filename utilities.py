import time 
import os
import sys
import math
sys.stdout.reconfigure(encoding='utf-8')
from colorama import Fore, Back, Style, init
#part = 8
#def = 10

class TextStyle:
    def __init__(self) -> None:
        init()

    def get_text(self, text: str, color: any = "", back: any = "") -> str:
        return color + back + str(text) + Style.RESET_ALL



class ProgressBar():
    def __init__(self, part) -> None:
        self.procent = 0
        self.all = math.ceil((10 + 8 * part) * 2.2)
        self.old = ""
    
    def progress(self, name):
        ts = TextStyle()
        print(f"\r {' ' * (self.all + len(self.old) + 10)}", end="")

        self.procent += 1
        bar = ts.get_text(text=" ", back=Back.WHITE) * self.procent + " " * (self.all - self.procent)
        procent = int((self.procent / self.all)  * 100)
        procent = ts.get_text(text=str(procent) + "%", color=Fore.GREEN)
        print(f"\r {procent} |{bar}|: {ts.get_text(name, color=Fore.CYAN)}", end="")

        self.old = name

bar: ProgressBar;

def start(part):
    global bar
    bar = ProgressBar(part=part)

def time_manager(func):
    def wrapper(*args, **kwargs):
        
        name = func.__name__
        t = time.time()
        bar.progress(f'Start: {name}')
        result = func(*args, **kwargs)
        time_stop = time.time() - t
        bar.progress(f'End: {name} with: {int(time_stop)}s')
        time.sleep(0.5)
        
        return result
    return wrapper