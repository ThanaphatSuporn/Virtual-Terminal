import os
import sys
import time
import platform
from pwinput import pwinput
from termcolor import colored,cprint
import requests
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

# List of colors to create the rainbow effect
colors = [
    Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA
]

# Function to print rainbow text
def print_rainbow(text):
    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end='', flush=True)
        time.sleep(0.001)  # Delay to make the effect visible
    print()  # To move to the next line after the rainbow text

# Sample text to print in rainbow colors
print_rainbow(" _______  _______  ______    __   __  _______ ")
print_rainbow("|       ||       ||    _ |  |  |_|  ||       |")
print_rainbow("|_     _||    ___||   | ||  |       ||    ___|")
print_rainbow("  |   |  |   |___ |   |_||_ |       ||   | __ ")
print_rainbow("  |   |  |    ___||    __  ||       ||   ||  |")
print_rainbow("  |   |  |   |___ |   |  | || ||_|| ||   |_| |")
print_rainbow("  |___|  |_______||___|  |_||_|   |_||_______|")


def cls():
    os.system("cls")

def reload():
   os.system("cls")
   os.system(r"python C:\Users\admin\OneDrive\เดสก์ท็อป\Folder_clean\Codling\Python\zcode\Virtual_terminal_Linux.py")

def neofetch():
    print(f"names:{platform.node()}")
    print(f"Operating System:{platform.system()}{platform.release()}")
    print(f"Processor:{platform.machine()}")

def help():
    print("Help Command terimnal Virtual")
    print("neofetch : Show OS information")
    print("clear : Clear terminal")
    print("help : Show this help")
    print("reload : Reload terminal")

def ls(directory):
    if os.path.exists(directory):  # Check if the directory exists
        lists = os.listdir(directory)
        for item in lists:
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):  # Only print directories
                cprint(f"{item}","light_blue")
            if os.path.isfile(item_path):  # Only print files
                cprint(f"{item}","light_green")
            time.sleep(0.0001)
    else:
        cprint(f"Directory '{directory}' does not exist.",'red')
        
def cd(directory):
    if os.path.exists(directory):
        os.chdir(directory)
    elif directory == '..':
        os.chdir('..')
    else:
        cprint('Directory does not exist','red')

def Terminal():
    while True:
        a = input(f"~[{os.getcwd()}]$")
        if a == "clear":
            cls()
        elif a == "reload":
            reload()
        elif a == "neofetch":
            neofetch()
        elif a.startswith("ls "):
            ls(a[3:])
        elif a == "ls":
            ls(os.getcwd())
        elif a.startswith("cd "):
            cd(a[3:])
        elif a == "help":
            help()
        else:
            cprint(f'Unknown Command : {a}','red')

Terminal()