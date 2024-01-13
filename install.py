import os
import sys
import time

def ascii_art():
    print("""
\033[92m   _____       _
  / ____|     (_)  \033[91m!!! INSTALLER !!!
\033[92m | (___  _ __  _ _ __   ___ _ __
  \033[92m\___ \| '_ \| | '_ \ / _ \ '__|
  ____) | | | | | |_) |  __/ |
 |_____/|_| |_|_| .__/ \___|_|
      v3.0      | |
                |_|\033[0m by JRDP Team  https://github.com/JRDPCN
""")

os.system("clear")
print("\n")
ascii_art()
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
if str(choice) =='Y' or str(choice)=='y':

    print("")
    time.sleep("")
    os.system("chmod 777 files/Sniper.py")
    print("")
    time.sleep("")
    os.system("chmod +x files/Sniper.py")
    print("")
    time.sleep("")
    os.system("mkdir /usr/share/Sniper")
    print("")
    time.sleep("")
    os.system("cp files/Sniper.py /usr/share/Sniper/Sniper.py")
    cmnd=(' #! /bin/sh \n exec python3 /usr/share/Sniper/Sniper.py "$@"')
    with open('/usr/bin/Sniper','w')as file:
        file.write(cmnd)
    os.system("chmod +x /usr/bin/Sniper & chmod +x /usr/share/Sniper/Sniper.py")
    print('''\n\n Sniper is installed successfully \nfrom now just type \x1b[6;30;42mSniper\x1b[0m in terminal. ''')
if str(choice)=='N' or str(choice)=='n':
    os.system("rm -r /usr/share/Sniper")
    os.system("rm /usr/bin/Sniper")
    print('[!] Sniper has been removed successfully.')
