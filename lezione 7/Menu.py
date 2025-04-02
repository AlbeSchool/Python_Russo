
scelta = ""

while scelta != "quit":
    print("-----MENÙ-----")
    print("a) gioca")
    print("b) calcola")
    print("c) saluta")
    print("quit) esci")
    print("--------------")
    scelta = str(input("Scegli una voce del menù: "))
    
    if scelta == "a":
        print("Hai scelto di giocare")
    elif scelta == "b":
        print("Hai scelto di calcolare")
    elif scelta == "c":
        print("Hai scelto di salutare")
    elif scelta == "quit":
        print("hai scelto di uscire")
    else:
        print("Scelta non valida, riprova")