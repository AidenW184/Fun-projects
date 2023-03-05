#!/usr/bin/env python3

import os

def menu(): 
    print("[1] TryHackMe VPN - VIP")
    print("[2] HackTheBox - VIP")
    print("[0] Exit")
    
def option1():
    print ("THM VPN Selected...")
    os.system('sudo openvpn *Location*')
def option2():
    print ("HTB VPN Selected...")
    os.system('sudo openvpn *Location*')

menu() 
option = int(input("Enter your option: "))

while option != 0: 
    if option == 1: 
        option1()
    elif option == 2:
        option2()
    else:
        print("Invalid option")

    print()
    menu() 
    option = int(input("Enter your option: "))
    
print("Goodbye")    
