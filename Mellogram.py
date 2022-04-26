import time

def jojo():
    print("\033[H\033[J")
bn = 7
n = 1

def silver():
    bn = 5
    n = 3
def bring():
    bn = 2
    n = 15
def gold():
    bn = 0.5
    n = 32

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
    print("[ 1 ] - Start a new game \n[ 2 ] - Continue what you started \n[ 3 ] - Settings \n[ 4 ] - Exit")
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
        print("Setting")
    elif answer == 4:
        jojo()
        hopy()

def killop():
    print("Hello, mountain, today we will mine. \n/Mine - start mining \n/Company - select a mining company \n/County - collected money \n/exit - go back ")
    
    mone()

kit = 0
def mone():
    global kit
    popi = str(input("> "))
    if popi == "/Mine" or popi == "/mine":
        tim()
        kit += n
        print(f'Money' + ' ' + str(kit))
        time.sleep(1)
        jojo()
        killop()
    elif popi == "/Company" or popi == "/company":
        jojo()
        biy = str(input("[ 1 ] Apple (100) \n[ 2 ] Sumsung (45) \n[ 3 ] Microsoft (23) \n>"))
        time.sleep(1)
        if biy == 3:
            if kit >= 23:
                kit - 23
                silver()
            else:
                print("You have less than the required amount")
        elif biy == 2:
            if kit >= 45:
                kit - 45
                bring()
            else:
                print("You have less than the required amount")
        elif biy == 1:
            if kit >= 100:
                kit - 100
                gold()
            else:
                print("You have less than the required amount")
        else:
            jojo()
            mone()
    elif popi == "/County" or popi == "/county":
        print(f'Money' + ' ' + str(kit))
        time.sleep(1)
        jojo()
        mone()
    elif popi == "/exit" or popi == "/exit":
        jojo()
        main()
    else:
        print("Unknown error")
        jojo()
        killop()

def hopy():
    bit = str(input("Exit? \n[ Yes ] [ No ] \n"))
    if bit == 'Yes' or bit == 'yes':
        exit()
    elif bit == 'No' or bit == 'no':
        jojo()
        main()
    else:
        print("Unknown error")

if __name__ == "__main__":
    main()
