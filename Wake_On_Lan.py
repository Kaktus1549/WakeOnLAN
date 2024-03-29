import time
from sys import platform
from colorama import Fore, Back, Style, init
from termcolor import colored
import shutil

init()

print(Fore.YELLOW + "Starting program.")
print(Fore.YELLOW + "Starting program..")
print(Fore.YELLOW + "Starting program...")

print(Fore.YELLOW + "Loading libaries.")
import os

print(Fore.YELLOW + "Succesfully loaded os library...")

import json

print(Fore.YELLOW + "Succesfully loaded JSON library...")
from wakeonlan import send_magic_packet

print(Fore.YELLOW + "Succesfully loaded WakeOnLan library...")
print(Fore.GREEN + "All libraries were succesfully loaded!!")
print(Fore.RESET)

# loading basic info about servers and starting
#ssh and servers
Server = {}

#classes, functions and variables
version = "2.7"
server_up = False
ssh_up = False
number = False
system_platform = platform
appdata_file = os.getenv('APPDATA')
current_dir = os.getcwd()

if system_platform == "win32" or system_platform == "win64":
    if not os.path.exists(appdata_file + "\\Server_starter"):
        os.makedirs(appdata_file + "\\Server_starter")
        file_path = appdata_file + "\\Server_starter\\"
    else:
        file_path = appdata_file + "\\Server_starter\\"
if system_platform == 'linux' or system_platform == "darwin":
    home_path = os.path.expanduser('~') + "/"
    if not os.path.exists(home_path + "Server_starter"):
        os.makedirs(home_path + "Server_starter")
        file_path = home_path + "Server_starter/"
    else:
        file_path = home_path + "Server_starter/"
class style:
   BOLD = '\033[1m'
   END = '\033[0m'
def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")
def sent_wakepacket(name):
    clear()
    print("Sending Wake on LAN packet to server => " + Server[name]['name'] + "\nWith parameters:")
    print("    - IP address: " + Server[name]['ipAddress'])
    ipaddres = Server[name]['ipAddress']
    print("    - Server port: " + Server[name]['wol'])
    ports = Server[name]['wol']
    macaddres = Server[name]['macAddress']
    print()
    send_magic_packet(macaddres, ip_address=ipaddres, port=int(ports))
    print("Wake On LAN packet was sent! Check server in while!")

def new_JSON():
    print(colored("JSON file wasn't found!! ", 'yellow', 'on_red'))
    time.sleep(1)
    print(colored("Creating new JSON file with basic parameters!! ", 'yellow', 'on_red'))
    if system_platform == "win32" or system_platform == "win64":
        if not os.path.exists(appdata_file + "\\Server_starter"):
            os.makedirs(appdata_file + "\\Server_starter")
            file_path = appdata_file + "\\Server_starter\\"
        else:
            file_path = appdata_file + "\\Server_starter\\"
    if system_platform == 'linux' or system_platform == 'darwin':
        home_path = os.path.expanduser('~') + "/"
        if not os.path.exists(home_path + "/Server_starter"):
            os.makedirs(home_path + "/Server_starter")
            file_path = home_path + "/Server_starter/"
        else:
            file_path = home_path + "/Server_starter/"

    with open( file_path + 'list.json', 'w') as file:
        Server['default']={
                "name": "Default",
                "ipAddress": "127.0.0.1",
                "macAddress": "FF:FF:FF:FF:FF:FF",
                "wol": "9"
        }
        save = json.dumps(Server, indent=4)
        file.write(save)
        time.sleep(1)
    print(Fore.GREEN + "JSON file was successfully created!!")
def save_JSON():
    try:
        with open(file_path +'list.json', 'w') as file:
            server_data = json.dumps(Server, indent=4)
            file.write(server_data)
    except:
        new_JSON()
        with open(file_path + 'list.json', 'w') as file:
            server_data = json.dumps(Server, indent=4)
            file.write(server_data)
def remove_JSON():
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
    else:
        print("JSON file was already removed!")

#commands
print(Fore.YELLOW + "Loading internal program commands...")

def help():
    print("""
    Welcome to the Starter server!
    This program is used to remotely wake up the server.
    This means you can start YOUR server from anywhere! And how can you do it?
    This program contains a set of basic commands, size of characters doesn't matter 
    (that is, you can write the "help" command as "hElP" and it will still work). 
    If you don't know the commands, just type "command list". 
    This command will list the commands and their descriptions. 
    
    """)
def command_list():
    print(style.BOLD + "\n List of all commands" +style.END + """
        
        HELP --> displays a welcome message containing basic information about the program
        COMMAND LIST --> Lists all commands available for this program
        CLEAR --> Clear terminal contents
        SERVER LIST --> Lists all available servers that can be boot on using Wake on LAN
        SERVER ON --> executes a chain of commands that will boot on the target server
        VERSION --> print out current version of program (there is going to be updates dont worry :) )
        EDITOR --> enables editor mode, you can edit server properties (his IPv4 address, MAC addres, etc.) or add new server to JSON file!
        PURGE --> deletes all related files (JSON, etc.)
        END --> saves and end this program, its easy as I say
        """)
def current_version():
    print(style.BOLD + """
Current version of program is --> """ + version + style.END + "\n")
def server_list(): 

    for i in Server:
        print("Detail information of server => " + style.BOLD + Server[i]['name'] + style.END)
        print(" ")
        for yes in Server[i]:
            if yes.lower() == 'ipaddress':
                print("    - IPv4 address: " + Server[i][yes])
            if yes.lower() == 'macaddress':
                print("    - MAC adress: " + Server[i][yes])
            if yes.lower() == 'wol':
                print("    - Wake on LAN port: " + Server[i][yes] + "\n\n")
    print(" ")
def server_on():
    print(style.BOLD + "Chose server from this list:" + style.END)

    for i in Server:
        print("    - " + Server[i]['name'])
    server_for_start = input("Server: ").lower()
    for i in Server:
        if server_for_start.lower() == Server[i]['name'].lower():
            server_for_start = i
    sent_wakepacket(server_for_start)
def editor():
    global number
    
    print(style.BOLD + "Welcome to server list editor! Choose action from list:")
    print(style.END )
    print("    1) Edit settings of existing server")
    print("    2) Add new server to list")
    print("    3) Remove server from list")
    choise = input("\nYour choice: ")
    while True:
        if choise == "1" or choise == "2" or choise == "3":
            break
        else:
            print(Fore.RED + "You entered unknown input, try again!" + Fore.RESET)
            print(style.BOLD + "Welcome to server list editor! Choose action from list:")
            print(style.END )
            print("    1) Edit settings of existing server")
            print("    2) Add new server to list")
            print("    3) Remove server from list")
            choise = input("Your choice: ")

    if choise == "2":
        clear()
        print("For adding new server to the list you are gonna need to know some basic info about server.")
        print("\n")
        server_name = input("Enter server name:")
        server_ip_address = input("Enter server IPv4 address:")
        server_MAC = input("Enter MAC address of server:")
        server_wol_port = input("Enter port of Wake on LAN:")
        print("\n")
        print(Fore.YELLOW + "Processing given information..")
        print("Processing empty inputs..." + Fore.RESET)
        if server_name == "":
            while True:
                print("You entered blank server name, try again")
                server_name = input("Enter server name:")
                if server_name != "":
                    break
        number = True
        server_ip_address_split = server_ip_address.split(".")
        for numbers in server_ip_address_split:
            if numbers.isdigit():
                pass
            else:
                number = False
        if server_ip_address == "" or number == False:
            i = False
            while i == False:
                print("You entered blank or invalid server IPv4 address, try again")
                server_ip_address = input("Enter server IPv4 address:")
                if server_ip_address != "":
                    server_ip_address_split = server_ip_address.split(".")
                    for numbers in server_ip_address_split:
                        if numbers.isdigit():
                            i = True 
                        else:
                            i = False
                            break
        if server_MAC == "":
            while True:
                print("You entered blank server MAC address, try again")
                server_name = input("Enter server MAC address:")
                if server_name != "":
                    break
        if server_wol_port == "" or int(server_wol_port.isdigit()) == False:
            while True:
                print("You entered blank or invalid Wake on LAN port, try again")
                server_wol_port = input("Enter Wake on LAN port:")
                if server_wol_port != "" or int(server_wol_port.isdigit()) != False:
                    break
        print(Fore.GREEN + "Done.." + Fore.RESET)
        print("Appending server to list..")
        Server[server_name] ={
            "name": server_name,
            "ipAddress": server_ip_address,
            "macAddress": server_MAC,
            "wol": server_wol_port
        }
        print("New server appended succesfully!")
        print("Saving JSON file..")
        save_JSON()
        print(Fore.GREEN + "Saved!" + Fore.RESET)
    if choise == "3":
        print(style.BOLD + "Chose server for deletion from this list:" + style.END)
        for i in Server:
            print("    - " + Server[i]['name'])
        server_for_delete = input("Server: ").lower()
        try:
            for i in Server:
                if server_for_delete.lower() == Server[i]['name'].lower():
                    server_for_delete = i
            Server.pop(server_for_delete)
            print("Server deleted, saving file..")
            save_JSON()
            print(Fore.GREEN + "Saved!" + Fore.RESET)
        except:
            print("An error occurred, maybe misspeled server name?")
    if choise == "1":
        print("\n")    
        print("Choose server for editing:")
        while True:

            for i in Server:
                print("    - " + Server[i]['name'])
            server_for_edit = input("Server: ").lower()
            for i in Server:
                if server_for_edit.lower() == Server[i]['name'].lower():
                    server_for_edit = i
                    no = True
                    break
                else:
                    no = False
            if no == True:
                break
            else:
                print("Unknown server, try it again!")

        while True:        
            print(style.BOLD + "Choose information you want edit:" + style.END)
            for yes in Server[server_for_edit]:
                if yes.lower() == 'name':
                    print(style.BOLD +"    1) Name: " + style.END + Server[server_for_edit][yes])
                if yes.lower() == 'ipaddress':
                    print(style.BOLD +"    2) IPv4 address: " + style.END + Server[server_for_edit][yes])
                if yes.lower() == 'macaddress':
                    print(style.BOLD +"    3) MAC address: " + style.END + Server[server_for_edit][yes])
                if yes.lower() == 'wol':
                    print(style.BOLD +"    4) Wake on LAN port: " + style.END + Server[server_for_edit][yes])
                
            print(style.BOLD + "    5) End session" + style.END)
            edit = input("Your choise: ")
            while True:
                if edit.isdigit():
                    break
                else:
                    print(Fore.RED + "Input must be ONLY digit!" + Fore.RESET)
                    edit = input("Your choise: ")
            if edit == '1':
                new_name = input("Enter new name: ")
                while True:
                    if new_name == "":
                        print("You cant enter blank name, try again!")
                        new_name = input("Enter new name: ")
                    else:
                        break
            else:
                new_name = Server[server_for_edit]['name']
            if edit == '2':
                new_IP = input("Enter new IPv4 address: ")
                numberr = True
                new_IP_split = new_IP.split(".")
                for numberss in new_IP_split:
                    if numberss.isdigit():
                        pass
                    else:
                        numberr = False
                if new_IP == "" or numberr == False:
                    i = False
                    while i == False:
                        print("Invalid or blank IPv4 address, try again!")
                        new_IP = input("Enter new IPv4 address: ")
                        if new_IP != "":
                            new_IP_split = new_IP.split(".")
                            for numberss in new_IP_split:
                                if numberss.isdigit():
                                    i = True 
                                else:
                                    i = False
                                    break
            else:
                new_IP = Server[server_for_edit]['ipAddress']
            if edit == '3':
                new_MAC = input("Enter new MAC address:")
                while True:
                    if new_MAC == "":
                        print("You cant leave MAC address blank, try again!")
                        new_MAC = input("Enter new MAC address:")
                    else:
                        break
            else:
                new_MAC = Server[server_for_edit]['macAddress']
            if edit == '4':
                new_WOL = input("Enter new Wake on LAN port: ")
                while True:
                    if new_WOL.isdigit() == False or new_WOL == "":
                        print("Invalid or blank Wake on LAN port, try again!")
                        new_WOL = input("Enter new Wake on LAN port: ")
                    else:
                        break
            else:
                new_WOL = Server[server_for_edit]['wol']
            if edit == '5':
                break     
            print("Processing and saving edited informations..")

            Server[server_for_edit] ={
                "name": new_name,
                "ipAddress": new_IP,
                "macAddress": new_MAC,
                "wol": new_WOL
            }
            save_JSON()
    print("Ending editor session...")

print(Fore.YELLOW + "Commands successfully loaded!!")

#JSON file with server info
print(Fore.YELLOW + "Loading list.json file with server's information...")

try:
    with open( file_path + 'list.json', 'r') as file:
        Server = json.loads(file.read())
except:
    new_JSON()

print(Fore.GREEN + "JSON file was succesfully loaded into memory!!")
print(Fore.MAGENTA + "Program was successfully started! Enjoy!!\n")
time.sleep(3)
clear()
print(colored("""
WARNING!!!

This program has been developed for personal use only. 
Any modification of the source code or the list.JSON file may lead to a fatal error that will cause the entire program to crash. 
If you don't know what the program does and HOW it does it, don't modify anything!!!

In case of errors, write to email --> helloiamkaktus@gmail.com

Press "ENTER" for continue:
""", 'green', 'on_red'))
while True:
    random_output = input()
    break
print("In case you dont know what to do use \"HELP\" command (no matter the size of the letters)")    

while True:

    current_input = input(Fore.YELLOW + "[" + Fore.LIGHTBLUE_EX + "root" + Fore.WHITE + "@" + Fore.LIGHTBLUE_EX + "server-wakeup" + Fore.YELLOW + "]" + Fore.GREEN + "#" + Fore.RESET)
    if current_input.lower() == 'help':
        help()
    elif current_input.lower() == "clear":
        clear()
    elif current_input.lower() == 'command list':
        command_list()
    elif current_input.lower() == 'version':
        current_version()
    elif current_input.lower() == 'server list':
        server_list()
    elif current_input.lower() == 'server on':
        server_on()
        server_up = False
    elif current_input.lower() == "editor":
        editor()
    elif current_input.lower() == "purge":
        remove_JSON()
    elif current_input.lower() == 'end':
        print(style.BOLD + Fore.RED + "Are you sure you want to end this program?" + Fore.RESET + style.END)
        check = input("Answer [Y/N]:")
        if check.lower() == 'y':
            break
        if check.lower() == 'n':
            print(Fore.YELLOW + "\nInterrupting shutdown.\n" + Fore.RESET)
        else:
            print(Fore.RED + "\nYou entered an invalid answer, interrupting shutdown.\n" + Fore.RESET)
    elif current_input == "":
        pass
    else:
        print(Fore.RESET + style.END + "\nYou entered unknown command!\n")

print(Fore.GREEN + "\nSaving program files...")

print("Saved JSON file...")
save_JSON()

print("Unloading program variables from memory...")
print(style.BOLD + Fore.LIGHTGREEN_EX + "Program was succesfully saved!")
time.sleep(2)

clear()
print("Program ends, thanks for using!" + style.END + Fore.RESET)