import time
import requests
import os,sys
from termcolor import colored
os.system('clear')
time.sleep(2)

print(colored("""

                 WELCOME TO BANgLADESH
                      BANgLADESH
                         V1.0 \n """, """green"""))


inp=input(colored("Target IP: ", "green"))
if inp.startswith('http://'):
	print(colored("                 Sorry, You cannot use 'http://' ", "cyan"))
	time.sleep(1)
	print(colored("         Shutting down...", "red"))
	time.sleep(4)
	sys.exit()
if inp.startswith("https://"):
	sys.exit("Sorry, You cannot use 'https://' ")
try:
	get=requests.get(f"http://api.hackertarget.com/reverseiplookup/?q={inp}")

	file=open("./Reversed-IPs.txt", "w")
	print(file.write(str(get.text)))
	print(colored(f"Successfull Identified total IPs from '{inp}' Check Reversed-IPs.txt !", "green"))
except Exception:
	print(colored(f" °.° The address you entered '{inp}' is not Connectable ! \n Or check your Internet Connections, \nThank you.", "red"))
