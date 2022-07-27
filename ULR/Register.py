import getpass
import ULR.Login
import modules.config as con
import KESH.Save as Save

ANS = ['Yes','Y','yes','y', 'Да', 'Д', 'да', 'д']

def jojo():
    print("\033[H\033[J")

class register:
	def __init__(self, NU, NP):
		self.NewUser = NU
		self.NewPassword = NP

	def Examination(self):
		if len(self.NewUser) > 256:
			deg = input("Name must not exceed 256 characters")
			jojo()
			DataReg()
		for i in list(self.NewUser):
			if i in ['~`!@#$%^&*()_+"№;%:?][}{|,.></']:
				deg = input("The name must not contain special characters")
				jojo()
				DataReg()
		Save.save(self.NewUser, self.NewPassword)

def DataReg():
	jojo()
	print('https://Mellogram.com/SesionUser/Registers/Register.html')
	NewUser = input("Login: ")
	NewPassword = getpass.getpass(prompt='Password: ', stream=None)
	jojo()
	l = register(NewUser, NewPassword)
	l.Examination()