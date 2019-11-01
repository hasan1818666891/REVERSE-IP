import time
import requests
import os,sys
from termcolor import colored
os.system('clear')
print(colored("               LOADING     (|)", "red"))
time.sleep(0.5)
os.system("clear")
print(colored("               LOADING.    (\)", "red"))
time.sleep(0.5)
os.system("clear")
print(colored("               LOADING..   (-)", "red"))
time.sleep(0.5)
os.system("clear")
print(colored("               LOADING...  (/)", "red"))
time.sleep(0.5)
os.system("clear")









print(colored("""


{
                                                             
########                                                     
##      ## *************************************             
#       ##    __Tutorial/Channel__[youtube.com/anonymousbghh]
########                                                     
########                                                     
#       ##    __Repository__[https://github.com/josifkhan/]  
##      ##    __Author_Name__[MD Josif Khan]                 
########_______________}                                     
                                                             
_________                    ________________________________
                                        BANgLADESH           
                                           V1.0 """          
,"""blue"""))
def rev():
	try:
		inp=input(colored("Target IP: ", "green"))
		if inp=='':
			print(colored("No Address found !", "cyan"))
			sys.exit()
		if inp.startswith('http://'):
			print(colored("                 Sorry, You cannot use 'http://' ", "cyan"))
			time.sleep(1)
			print(colored("         Shutting down...", "red"))
			time.sleep(3)
			sys.exit()
		if inp.startswith("https://"):
			sys.exit("Sorry, You cannot use 'https://' ")

		get=requests.get(f"http://api.hackertarget.com/reverseiplookup/?q={inp}")
		file=open(f"./{inp}.txt", "w")
		if get.text== "error check your search parameter":
			sys.exit(colored(f" '{inp}' is not a valid address !", "yellow"))
		else:
			print(file.write(str(get.text)))
			print(colored(f"Successfully Identified total IPs from '{inp}' ! Check {inp}.txt file.", "green"))
	except Exception:
		print(colored(f" °.° The address you entered '{inp}' is not Connectable ! \n Or check your Internet Connections, \nThank you.", "red"))
	except KeyboardInterrupt:
		x=input(colored("\n[!] Did you just try to quit application ? Y/n: ","yellow"))
		if x=="Y" or x=="y":
			print(colored("[!] Thank you for using 'reverse-eb' .","cyan"))
			time.sleep(1)
			print(colored("[!] Shutting down application...","red"))
			time.sleep(2)
			sys.exit("[!] Done.")
		elif x=="N" or x=="n":
			rev()
		else:
			sys.exit(colored("[!] Application disconnected.","red"))
rev()
