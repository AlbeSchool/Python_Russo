#Crea un programma per indovinare un numero segreto. fino a quando l'utente non inserisce il numero corretto composto da 3 cifre il programma continuerà a dirgli che non è possibile entrare. Ci sono un massimo di 4 tentativi
# esempuo numSegreto 123



numSegreto = 123
tentativi = 4

while numSegreto != 123 and tentativi > 4:
    numUtente = int(input("Inserisci un numero segreto composto da 3 cifre: "))
    
    if numUtente == numSegreto:
        print("Hai indovinato il numero segreto!")
    else:
        tentativi -= 1
        print("Numero errato! Hai ancora {tentativi} tentativi.")




numSegreto = 123
tentativi = 4

while tentativi > 0:
    # Chiedi all'utente di inserire il numero
    numUtente = int(input("Inserisci un numero segreto composto da 3 cifre: "))
    
    if numUtente == numSegreto:
        print("Hai indovinato il numero segreto!")
    elif numUtente < 100 or numUtente > 999:
        print("Il numero deve essere composto da 3 cifre.")
    elif tentativi == 0:
        print("Hai esaurito i tentativi!")
    else:
        tentativi -= 1
        print (f"Numero Errato! hai ancora {tentativi} tentativi.")
