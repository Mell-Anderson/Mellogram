import ULR.Login, ULR.Register
import Mellogram as Mell
import modules.config as con

def profile():
    ProfileAcces = input("I suggest logging in to help you save your score.\n[1] Login\n[2] Logout\n[3] Register\n[4] Exit\n> ")
    if ProfileAcces == '1':
        ULR.Login.DataLog()
        Mell.main()
    elif ProfileAcces == '2':
        con.init()
        con.UserName = 'Unknown'
        Mell.main()
    elif ProfileAcces == '3':
        ULR.Register.DataReg()
        Mell.main()
    elif ProfileAcces == '4':
        Mell.jojo()
        exit()