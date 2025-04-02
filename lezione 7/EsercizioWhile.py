# Crea un programma che legge un numero inserito da un utente e stabolosce se questo numero è pari o dispari. # il programma si interrome se l'utente inserisce il numero 0

# se il numero diviso per 2 è intero allora è pari
# se il numero diviso per 2 non è intero allora è dispari


numero = ""
while numero != 0:
    numero = int(input("Inserisci un numero (0 per uscire): "))
    
    if numero == 0:
        print("Hai scelto di uscire")
    elif numero % 2 == 0:
        print("Il numero è pari")
    else:
        print("Il numero è dispari")