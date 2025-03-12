print("scrivimi il tuo nome caro utente!")

# per poter aquisire qualcosa che digita l'utente uso input

nomeUser = input() #argomento mancante

print("Benvenuto", nomeUser)

# faccio la stessa cosa in modo più veloce passando come argomento all'input della frase
#funzione (argomento) --> tutto questo si chiama firma del METODO
cognomeUser = input("scrivi il tuo cognome..")
print("il tuo cognome è", cognomeUser)


print("--------------NUMERI--------------")
#tutto chio che rcuper da untente è considerato una stringa, un testo. 
# Per poter fare un calcolo devo fare il type casting, ovvero forzare quella variabile ad essere un numero e non una stringa
num1 = int( input("scrivi un numero" ))
num2 = int( input("scrivi un altro numero" ))
somma = num1 + num2
print("la somma vale: ", somma)


#esempio con int

num3 = int("3") #type casting
num4 = int 6 #Number -> int
somma2 = num3 + num4
print(somma2)