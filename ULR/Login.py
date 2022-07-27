import getpass
import ULR.Register
import Mellogram as Mell
import KESH.Load as ld

ANS = ['Yes','Y','yes','y', 'Да','Д','да','д']

def jojo():
    print("\033[H\033[J")

class login:
    def __init__(self, UN, UP):
        self.UserName = UN
        self.__UserPassword = UP

    def Examination(self):
        if self.UserName == ld.NameFile and self.__UserPassword == ld.Password:
            con.UserName = self.UserName
            ld.load(self.UserName, self.__UserPassword)
            Mell.main()
        else:
            dog = input("Try again?")
            if dog in ANS:
                DataLog()
            else:
                Mell.main()

def DataLog():
    jojo()
    if ld.NameFile != None:
        print('https://Mellogram.com/SesionUser/Logins/Login.html')
        UserName = input("Login: ")
        UserPassword = getpass.getpass(prompt='Password: ', stream=None)
        jojo()
        l = login(UserName, UserPassword)
        l.Examination()
    else:
        Mell.main()