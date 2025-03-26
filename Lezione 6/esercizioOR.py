nome = input("Ciao, come ti chiami?")

benvenuto = "Ciao " + nome +", il professore è buono o cattivo? " 

professore = input(benvenuto)

if professore == "buono":
    esameScritto = bool(input("Hai superato lo scritto? "))
    esameOrale = bool(input("Hai superato l'orale? "))
    if esameScritto or esameOrale:
        print("Complimenti hai superato l'esame")
    else:
        print("Mi dispiace, non hai superato l'esame")
elif professore == "cattivo":
    esameScritto = bool(input("Hai superato lo scritto? "))
    esameOrale = bool(input("Hai superato l'orale? "))
    if esameScritto and esameOrale:
        print("Complimenti hai superato l'esame")
    else:
        print("Mi dispiace, non hai superato l'esame")
