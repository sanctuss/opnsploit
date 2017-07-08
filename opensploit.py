#!/usr/bin/python3.6

#Author: sanctus
#2017 year

import os
import sys
import random
import socket
import getpass

def show_random_banner():
    try:
        os.chdir("banners")
        lol = os.listdir()
        f = open(lol[random.randint(1, len(lol))])
        data = f.read()
        print(data)
        f.close()
        os.chdir("..")
    except:
        print("[-] banners dir is unavaible. quiting")
        sys.exit()

def show_promt():
    hostname = socket.gethostname()
    username = getpass.getuser()
    print(username + '@' + hostname + " >")

def if_command_right(command):
    commands[9] = {"help", "run", "show", "search", "use", "banner", "connect", "set", "exit"}
    if command in commands:
        return True
    else:
        return False

def use(command):
    try:
        os.chdir(command)
    except:
        print("[-] ooooops, i dont know what means: " +  command)
#def connect(command):

def run(argv):
    comm = "exploit" + argv
    os.system(comm)

def show_options():
    try:
        f = open("options", 'r')
        data = f.read()
        print(data)
    except:
        print("[-] there are no options file. Is it exists?")

def execute_command(command):
    if "help" in command:
        print("add later")
   # if "run" in command:
        
   # if command == "show":
        
   # if command == "search":

   # if command == "use":
  #      use(command)
    if command == "banner":
        show_random_banner()
 #   if command == "connect":
    
#    if command == "set":

    if command == "exit":
        print("[!] goodbye.")
        sys.exit()

if __name__ == "__main__":
    #show banner
    show_random_banner()
    command = "LOLOLOLOLOLOLOLOL, You are loooser"
    while True:
        #promt
        #show_promt()
        #commands input and executing
        try:
            command = input(show_promt())
            #logic is my passion:)
            if if_command_right(command):
                execute_command(command)
            else:
                print("[!] oooooops, looking like you typed wrong command :[")
        except KeyboardInterrupt:
            print("You are lazy motherfucker, use exit to exit")


