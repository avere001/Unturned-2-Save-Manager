import _winreg as winreg
import os

KEY_NAME = "Software\\Smartly Dressed Games\\Unturned"
u2key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_NAME);

def getChoice(prompt, *args):
	
	args = map(str,args)
	
	choice = None
	while not choice in args:
		choice = raw_input(prompt)
	return choice

def exportKey():
	
	while True:
		fname = raw_input("Save as (.reg): ") + ".reg"
		
		if os.path.exists(fname):
			choice = getChoice("File exists! overwrite?:", 
					"yes","no","y","n")
			if choice == "no" or choice == "n":
				continue
			else:
				os.remove(fname)

		winreg.SaveKey(u2key, fname)
		
def importKey():
	
	files = [f for f in os.listdir(".") if f.endswith('.reg')]
	if len(files) == 0:
		print "Nothing to import!"
		return
	for f in files:
		print "{}) {}".format(files.index(f)+1, f)
	choice = files[int(getChoice("Select a file: ", *range(1,len(files))))-1]
	winreg.LoadKey(winreg.HKEY_CURRENT_USER, KEY_NAME, choice)

while True:
	print "1) Import Save"
	print "2) Export Save"
	print "3) Delete Save"
	print "4) Exit"
	choice = int(getChoice("Select an option (1-4): ",1,2,3,4))
	
	if choice == 1:
		importKey()
	elif choice == 2:
		exportKey()
	elif choice == 3:
		deleteKey()
	elif choice == 4:
		break
