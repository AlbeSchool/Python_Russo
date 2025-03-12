# Permetti all'utente di inserire 2 numeri interi e calcola il risultato delle seguenti operazioni
# + - * / **2

num1 = int(input("Inserisci un numero "))
num2 = int(input("Insrisci un numero "))

somma1 = num1 + num2
sottrazione1 = num1 - num2
somma2 = num1 * num2
divisione1 = num1 / num2
potenza1 = num1 **2
potenza2 = num2 **2 

print("la somma dei tuoi numeri addizionati è ", somma1)
print("la sottrazione dei tuoi numeri è ", sottrazione1)
print("la somma dei tuoi numeri moltiplicati è ", somma2)
print("la divisione dei tuoi numeri è ", divisione1)
print("la potenza dei tuo primo numero è ", potenza1)
print("la potenza dei tuo secondo numero è ", potenza2)