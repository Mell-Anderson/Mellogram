import time

nip = 0
bn = 0.1
n = 100

def jojo():
    print("\033[H\033[J")
    
def tim():
    jojo()
    print("0%[•••••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("5%[#••••••••••••••••••]")
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
    print("100%[###################]")
    time.sleep(bn)
    jojo()

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
        time.sleep(1)
        jojo()
        main()
    elif answer == 3:
        jojo()
        print("Under development")
        dog = input("> ")
        time.sleep(1)
        jojo()
        main()
    elif answer == 4:
        jojo()
        print("Under development")
        dog = input("> ")
        time.sleep(1)
        jojo()
        main()
        #jojo()
        #print("Setting")
        #kode = str(input("Kode: "))
        #if kode == "God":
            #god()
            #print("Well good, your account is replenished with 1000 coins")
            #time.sleep(2)
            #jojo()
            #main()
        #else:
            #print("Error kodes")
            #time.sleep(1)
            #jojo()
            #main()
    elif answer == 5:
        jojo()
        hopy()

def silver():
    global kit, bn, n
    gin = kit - 100
    bn = 0.5
    n = 32

def killop():
    jojo()
    print("Hello, mountain, today we will mine. \n/Mine - start mining \n/Company - select a mining company \n/County - collected money \n/exit - go back ")
    mone()

def mone():
    global nip
    popi = str(input("> "))
    if popi == "/Mine" or popi == "/mine":
        tim()
        nip += n
        if git == "gir":
            print(f'Money' + ' ' + str(gin))
        else:
            print(f'Money' + ' ' + str(nip))
        time.sleep(1)
        jojo()
        killop()
    elif popi == "/Company" or popi == "/company":
        jojo()
        biy = str(input("[ 1 ] Apple (100) \n[ 2 ] Sumsung (45) \n[ 3 ] Microsoft (23) \n> "))
        time.sleep(1)
        if biy == 1:
            if nip >= 100:
                silver()
                git = "gir"
                print("You have acquired company assets")
                time.sleep(1)
                jojo()
                killop()
            else:
                print("You have less than the required amount")
                time.sleep(1)
                jojo()
                killop()
        #elif biy == 2:
            #if kit >= 45:
            #    kit -= 45
            #    bn = 2
            #    n = 15
            #else:
            #    print("You have less than the required amount")
        #elif biy == 1:
            #if kit >= 100:
            #    
            #else:
            #    print("You have less than the required amount")
        else:
            jojo()
            killop()
    elif popi == "/County" or popi == "/county":
        if git == "gir":
            print(f'Money' + ' ' + str(gin))
        else:
            print(f'Money' + ' ' + str(kit))
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

if __name__ == "__main__":
    main()