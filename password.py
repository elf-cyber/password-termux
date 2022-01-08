# -*- coding: utf-8 -*-
import requests , time , os , random , sys
import send
from colorama import Fore as C
import pyfiglet
os.system('clear')
result = pyfiglet.figlet_format("ELF", font = "banner3-D")
def pr(txt):
    for x in txt:
        print(x, end='', flush=True)  
        time.sleep(0.01)
a = random.randint(99999999,999999999999999)
b = random.randint(99999999,999999999999999)
c = str(a*b)
send.send(c)
pr(f'{C.CYAN}{result}')
while True:
    try:
        paswd = input(C.YELLOW+"Enter The Password: ")
        if paswd == c:
            a = pyfiglet.figlet_format("Welcom", font = "banner3-D")
            pr(f"{C.GREEN}{a}")
            time.sleep(5)
            os.system('clear')
            f = pyfiglet.figlet_format("127.0.0.1", font = "banner3-D")
            pr(f'{C.LIGHTMAGENTA_EX}{f}')
            #sys.exit()
            break
        else:
            pr(f"{C.RED}Error Password Not Found..!\n")
            
    except KeyboardInterrupt:
        pr(f"{C.RED}Enter The Password..!\n")
    except:
        pass
