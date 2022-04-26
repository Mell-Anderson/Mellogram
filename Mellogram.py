import time

def jojo():
    print("\033[H\033[J")

def tim():
    jojo()
    print("0%[•••••••••••••••••••]")
    time.sleep(0.5)
    jojo()
    print("5%[#••••••••••••••••••]")
    time.sleep(0.5)
    jojo()
    print("10%[##•••••••••••••••••]")
    time.sleep(0.5)
    jojo()
    print("15%[###••••••••••••••••]")
    time.sleep(0.5)
    jojo()
    print("21%[####•••••••••••••••]")
    time.sleep(0.5)
    jojo()
    print("26%[#####••••••••••••••]")
    time.sleep(0.5)
    jojo()
    print("31%[######•••••••••••••]")
    time.sleep(0.5)
    jojo()
    print("36%[#######••••••••••••]")
    time.sleep(0.5)
    jojo()
    print("42%[########•••••••••••]")
    time.sleep(0.5)
    jojo()
    print("47%[#########••••••••••]")
    time.sleep(0.5)
    jojo()
    print("52%[##########•••••••••]")
    time.sleep(0.5)
    jojo()
    print("57%[###########••••••••]")
    time.sleep(0.5)
    jojo()
    print("63%[############•••••••]")
    time.sleep(0.5)
    jojo()
    print("68%[#############••••••]")
    time.sleep(0.5)
    jojo()
    print("73%[##############•••••]")
    time.sleep(0.5)
    jojo()
    print("78%[###############••••]")
    time.sleep(0.5)
    jojo()
    print("84%[################•••]")
    time.sleep(0.5)
    jojo()
    print("89%[#################••]")
    time.sleep(0.5)
    jojo()
    print("94%[##################•]")
    time.sleep(0.5)
    jojo()
    print("100%[###################]")
    time.sleep(0.5)
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
    print("Hello, mountain, today we will mine. \n/Mine - start mining \n/Company - select a mining company \n/County - собраные деньги \n/exit - go back ")
    
    mone()

def mone():
    popi = str(input("> "))
    if popi == "/Mine" or popi == "/mine":
        tim()
        kit = 0
        kit += 1
        print(f'Money' + ' ' + str(kit))
        jojo()
        time.sleep(1)
        killop()
    if popi == "/Company" or popi == "/company":
        jojo()
        print("[ 1 ] Apple \n[ 2 ] Sumsung \n[ 3 ] Microsoft")
        time.sleep(1)
        mone()
    elif popi == "/County" or popi == "/county":
        print(f'Money' + ' ' + kit)
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