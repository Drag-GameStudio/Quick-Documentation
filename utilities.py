import time 
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

#part = 8
#def = 10

class ProgressBar():
    def __init__(self, part) -> None:
        self.procent = 0
        self.all = 10 + 8 * part
    
    def progress(self, name):
        print(f"\r {" " * 100}", end="")
        self.procent += 1
        bar = "#" * self.procent + " " * (self.all - self.procent)
        procent = int((self.procent / self.all)  * 100)
        print(f"\r {procent}% |{bar}|: {name}", end="")

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