import os
try:
    import colorama
    import pyfiglet
    import random
    import time as t
    import urllib.parse
    import urllib.request
    import update_check
except ModuleNotFoundError:
    print("run setup.py")
    exit()
from colorama import *
print(Fore.CYAN + "This tool help in generating strong password which is hard to be guessed.")
t.sleep(2.9)
os.system("clear")
print(Fore.RED + "Warning: Make sure you save the password in a safe place")
t.sleep(3)
from update_check import isUpToDate, update
if isUpToDate(__file__,  "https://raw.githubusercontent.com/De-Technocrats/Password-Generator/main/password.py") == False:
    print(Fore.YELLOW+ "This version is outdated, will update the tool in a minute")
    t.sleep(3)
    update("password.py",  "https://raw.githubusercontent.com/De-Technocrats/Password-Generator/main/password.py")
    print(Fore.GREEN + "Updated\nRun tool again")
    exit()
def loop():
    os.system("clear")
    head = pyfiglet.figlet_format("Password-Generator")
    print (Fore.YELLOW + head)
    print(Fore.RED + " Version 1.0".center(60))
    print(Fore.YELLOW + "[+] " + Fore.GREEN + "Tool Name:Password-Generator\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Developer:Spider Anongreyhat(Anonspidey)\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Version:1.0\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Team:De Technocrats\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Github:https://github.com/spider863644\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "WhatsApp:+2349052863644")
    print(Fore.RED + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>" + Fore.CYAN + "Choose a valid option" + Fore.RED + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(Fore.BLUE + """
[1] Generate password
[2] Join our WhatsApp group
[3] Join our telegram channel
[4] Let's collaborate on my next tool
[5] Exit program
""")
    try:
        option = int(input(Fore.YELLOW + Back.RED + "Enter an option: " + Style.RESET_ALL + " "))
    except:
        print(Fore.RED + "Only integers is allowed")
        t.sleep(3)
        loop()
    if option == 1:
        os.system("clear")
        try:
            pass_len = int(input(Fore.GREEN + "Enter passwor length: "))
        except ValueError:
            print(Fore.RED + "Value must be numerical !")
            t.sleep(3)
            loop()
        if pass_len < 10:
                print(Fore.RED + "Password length must be greater than or equal to 10!")
                t.sleep(3)
                loop()
        Sname = input(Fore.GREEN + "Enter surname: ")
        Fname = input(Fore.GREEN + "Enter first name: ")
        Lname = input(Fore.GREEN + "Enter last name: ")
        phone_num = input(Fore.GREEN + "Enter phone number: ")
        try:
            alpha_length = int(input(Fore.GREEN + "Enter alphabet length: "))
            num_length = int(input(Fore.GREEN + "Enter numeric length: "))
            special_char_length = int(input(Fore.GREEN + "Enter s.pecial character length: "))
        except ValueError:
            print(Fore.RED + "Value must be numerical!")
            t.sleep(3)
            loop()
        if alpha_length + num_length + special_char_length > pass_len:
            print(Fore.RED + "combined length is greater than password length")
            t.sleep(3)
            loop()
        elif alpha_length + num_length + special_char_length < pass_len:
           print(Fore.RED + "Combined length is lesser than password length")
           t.sleep(3)
           loop()
        print(Fore.YELLOW + "generating password...")
        combined_names = Sname + Fname + Lname
        alpha = combined_names[-alpha_length:]
        num = phone_num[-num_length:]
        special_char = "~|√π÷×¶∆£€$¢^={}\\℅#[]<>_&-+()/*\!"
        special = special_char[-special_char_length:]
        os.system("clear")
        password = alpha +special + num
        print(Fore.GREEN + "Generated password is: " + Fore.YELLOW + password)
    elif option == 2:
        os.system("xdg-open https://chat.whatsapp.com/IWqGOsJPjkp2vXcMSJKYns")
        loop()
    elif option == 3:
        os.system("xdg-open https://t.me/termuxhackz_society")
        loop()
    elif option == 4:
        message = {'tex' : """I would like to collaborate with you,when developing your next tool
        
        Do not forget to tell me when you are ready to create another tool
        
        Thanks 🙏🙏"""}
        data = urllib.parse.urlencode(message)
        send_message = "xdg-open https://wa.me/09052863644?" + data
        os.system(send_message)
        loop()
    elif option == 5:
        exit()
    else:
        print(Fore.RED + "Invalid option!")
        t.sleep(3)
        loop()
loop()