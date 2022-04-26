import time

#import datetime
#x = datetime.datetime.now()
#timeS = str(x.strftime("%X"))
#"[" + timeS + "]" + 

nip = 0
bn = 7
n = 5

Apple = "hor"
Sumsung = "hor"
Microsoft = "hor"

def jojo():
    print("\033[H\033[J")
    
def tim():
    global nip
    jojo()
    print("0%[••••••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("5%[#•••••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("10%[##•••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("15%[###••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("21%[####•••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("26%[#####••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("31%[######•••••••••••••]")
    time.sleep(bn)
    jojo()
    print("36%[#######••••••••••••]")
    time.sleep(bn)
    jojo()
    print("42%[########•••••••••••]")
    time.sleep(bn)
    jojo()
    print("47%[#########••••••••••]")
    time.sleep(bn)
    jojo()
    print("52%[##########•••••••••]")
    time.sleep(bn)
    jojo()
    print("57%[###########••••••••]")
    time.sleep(bn)
    jojo()
    print("63%[############•••••••]")
    time.sleep(bn)
    jojo()
    print("68%[#############••••••]")
    time.sleep(bn)
    jojo()
    print("73%[##############•••••]")
    time.sleep(bn)
    jojo()
    print("78%[###############••••]")
    time.sleep(bn)
    jojo()
    print("84%[################•••]")
    time.sleep(bn)
    jojo()
    print("89%[#################••]")
    time.sleep(bn)
    jojo()
    print("94%[##################•]")
    time.sleep(bn)
    jojo()
    print("100%[##################]")
    time.sleep(bn)
    jojo()
    nip += n

def ast():
    global nip, bn, n
    nip -= 100
    bn = 5
    n = 50

def ast2():
    global nip, bn, n
    nip -= 45
    bn = 3
    n = 30

def ast3():
    global nip, bn, n
    nip -= 23
    bn = 1
    n = 10

def god():
    global nip
    nip += 1000

def speed():
    global bn, n
    bn = 0.1
    n = 1000
   
def setting(): 
    print("Setting")
    kode = str(input("Kode: "))
    if kode == "God":
        god()
        print("Well good, your account is replenished with 1000 coins")
        time.sleep(2)
        jojo()
        main()
    elif kode == "Speed":
        speed()
        print("Well good, your parameters are increased")
        time.sleep(2)
        jojo()
        main()
    else:
        print("Error kodes")
        time.sleep(1)
        jojo()
        main()

def main():
    print("Hello, well, I think you know me, but that doesn't stop us from talking")
    print("[ 1 ] - Start a new game \n[ 2 ] - Continue what you started \n[ 3 ] - Shop \n[ 4 ] - Settings \n[ 5 ] - Exit")
    answer = int(input("> "))
    if answer == 1:
        killop()
        jojo()
    elif answer == 2:
        jojo()
        print("Under development")
        dog = input("> ")
        jojo()
        main()
    elif answer == 3:
        jojo()
        print("Under development")
        dog = input("> ")
        jojo()
        main()
    elif answer == 4:
        jojo()
        setting()
    elif answer == 5:
        jojo()
        hopy()
    else:
        jojo()
        main()

def killop():
    jojo()
    print("Hello, mountain, today we will mine. \n/Mine - start mining \n/Company - select a mining company \n/County - collected money \n/exit - go back ")
    mone()

def mone():
    global nip, Apple, Sumsung, Microsoft
    popi = str(input("> "))
    if popi == "/Mine" or popi == "/mine":
        pop = int(input("Сколько желаете запустить ферм?(0/5) \n> "))
        if pop == 1:
            tim()
        elif pop == 2:
            tim()
            time.sleep(0.5)
            tim()
        elif pop == 3:
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
        elif pop == 4:
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
        elif pop == 5:
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
        else:
            jojo()
            mone()
        print(f'Money' + ' ' + str(nip))
        time.sleep(1)
        jojo()
        killop()
    elif popi == "/Company" or popi == "/company":
        jojo()
        biy = int(input("[ 1 ] Apple (100) \n[ 2 ] Sumsung (45) \n[ 3 ] Microsoft (23) \n> "))
        time.sleep(1)
        if biy == 1:
            if nip >= int(100) and Apple == "hor":
                ast()
                jojo()
                print("Your money was transferred to the company")
                Apple = "horo"
                dog = input("> ")
                jojo()
                killop()
            else:
                jojo()
                print("You have less than the required amount, or you already have assets of this company")
                dog = input("> ")
                jojo()
                killop()
            if biy == 2:
                if kit >= int(45) and Sumsung == "hor":
                    ast2()
                    jojo()
                    print("Your money was transferred to the company")
                    Sumsung = "horo"
                    dog = input("> ")
                    jojo()
                    killop()
                else:
                    jojo()
                    print("You have less than the required amount")
                    dog = input("> ")
                    jojo()
                    killop()
            if biy == 3:
                if kit >= int(23) and Microsoft == "hor":
                    ast3()
                    jojo()
                    print("Your money was transferred to the company")
                    Microsoft = "horo"
                    dog = input("> ")
                    jojo()
                    killop()
                else:
                    jojo()
                    print("You have less than the required amount, or you already have assets of this company")
                    time.sleep(1)
                    jojo()
                    killop()
        else:
            jojo()
            killop()
    elif popi == "/County" or popi == "/county":
        print(f'Money' + ' ' + str(nip))
        time.sleep(1)
        jojo()
        killop()
    elif popi == "/exit" or popi == "/exit":
        jojo()
        main()
    else:
        print("Unknown error")
        jojo()
        killop()

def hopy():
    bit = str(input("Exit? \n[ Yes ] [ No ] \n> "))
    if bit == 'Yes' or bit == 'yes':
        exit()
    elif bit == 'No' or bit == 'no':
        jojo()
        main()
    else:
        print("Unknown error")
        jojo()
        main()

if __name__ == "__main__":
    main()