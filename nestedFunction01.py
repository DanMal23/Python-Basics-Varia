
def pacman(info="Arch Linux"):

	def pm(): #function inside a function
		return "This OS uses pacman "
	def pm_other():
		return "This OS uses other package manager, not pacman"

	if info =="Arch Linux" or info =="AcroLinux": # Python uses 'or', C++ or Java use '||'
		return pm
	elif info =="Antergos":
		return pm
	elif info =="Manjaro Linux":
		return pm
	elif info =="Chakra Linux":
		return pm
	
	else: 
		return pm_other

a=pacman()
print(a)
print(a())