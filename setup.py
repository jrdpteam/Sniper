import os
import time
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system("clear")

def print_ascii_art():
    print(f'''{Fore.RED}
   _____       _
  / ____|     (_)  {Style.RESET_ALL}{Fore.GREEN}!!! INSTALLER !!!{Style.RESET_ALL}{Fore.RED}
 | (___  _ __  _ _ __   ___ _ __
  \___ \| '_ \| | '_ \ / _ \ '__|
  ____) | | | | | |_) |  __/ |
 |_____/|_| |_|_| .__/ \___|_|
      v3.0      | |
                |_| by JRDP Team  https://github.com/JRDPCN
    ''' + Style.RESET_ALL)

def install_sniper():
    print("\nInstalling Sniper...")
    time.sleep(0.5)
    os.system("chmod 777 files/Sniper.py")
    time.sleep(0.5)
    os.system("chmod +x files/Sniper.py")
    time.sleep(0.5)
    os.system("mkdir -p /usr/share/Sniper")
    time.sleep(0.5)
    os.system("cp files/Sniper.py /usr/share/Sniper/Sniper.py")
    cmnd = '#! /bin/sh \n exec python3 /usr/share/Sniper/Sniper.py "$@"'
    with open('/usr/bin/Sniper', 'w') as file:
        file.write(cmnd)
    os.system("chmod +x /usr/bin/Sniper && chmod +x /usr/share/Sniper/Sniper.py")

    success_message = "Sniper is installed successfully.\nFrom now on, just type 'sudo Sniper' in the terminal."
    subprocess.Popen(["zenity", "--info", "--text", success_message, "--title", "Success"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def uninstall_sniper():
    print("\nUninstalling Sniper...")
    time.sleep(0.5)
    os.system("rm -r /usr/share/Sniper")
    os.system("rm /usr/bin/Sniper")

    success_message = "Sniper has been uninstalled successfully."
    subprocess.Popen(["zenity", "--info", "--text", success_message, "--title", "Success"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main_menu():
    clear_screen()
    print_ascii_art()
    print("\nMenu:")
    print("1. Install Sniper")
    print("2. Uninstall Sniper")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")
    return choice

if __name__ == "__main__":
    while True:
        choice = main_menu()

        if choice == '1':
            install_sniper()
        elif choice == '2':
            uninstall_sniper()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
            time.sleep(1)
