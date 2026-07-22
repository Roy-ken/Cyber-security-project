import os
from pathlib import Path
import socket

os.system("clear")

GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
RESET = "\033[0m"


user_input=""

print(RED)
print(r"""
  ██████╗  ██████╗ ██╗   ██╗
  ██╔══██╗██╔═══██╗╚██╗ ██╔╝
  ██████╔╝██║   ██║ ╚████╔╝
  ██╔══██╗██║   ██║  ╚██╔╝
  ██║  ██║╚██████╔╝   ██║
  ╚═╝  ╚═╝ ╚═════╝    ╚═╝

  _______ROY_THE_HACKER_____
""")
print(GREEN)
print("_____Created by Roy")
print("_____version 0.1.2")
print("_____cybersecurity framework")
print("_____type help to list all commands")
print(RESET)

def help():
    print(GREEN)
    print("""commands:

File:
search___search for a file
list_____list contents in a directory

Network:
info_____get network information
scan_____scan for open ports

Terminal:
help_____open this interface
clear____clear text on terminal
exit_____exit console

""")

def info():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()

    print("Local IP:", local_ip)

def scanner():
    target = input(BLUE+"Enter IP: ")

    for port in range(20, 25):
        s = socket.socket()
        s.settimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()


def search():
    directory = input(BLUE+"Enter directory path: "+RESET)
    filename = input(BLUE+"Enter file name to search: "+RESET)
    found = False
    print(GREEN)
    print("starting search")
    for root, dirs, files in os.walk(directory):
        if filename in files:
            print(f"Found: {os.path.join(root, filename)}")
            found = True

    if not found:
        print("File not found.")


def list():
    print(GREEN+os.getcwd())
    user_path = input(BLUE+"enter directory: "+RESET)
    directory = Path(user_path)

    for item in directory.iterdir():
        if item.is_dir():
            print(GREEN+f"[DIR]  {item.name}")
        else:
            print(PURPLE+f"[FILE] {item.name}")




while True:
    user_input=input(RED + "roy~ " + RESET)
    if user_input == "search":
        search()
        print(RESET)
    elif user_input == "list":
        list()
        print(RESET)
    elif user_input == "clear":
         os.system("clear")
    elif user_input == "help":
        help()
        print(RESET)
    elif user_input == "exit":
        break
    elif user_input =="info":
        info()
    elif user_input =="scan":
        scanner()