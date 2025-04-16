#ESERCIZIO 2
#Data la seguente lista di numeri:
# 1. Trova i Numeri Pari
# 2. Calcola la Somma dei Numeri Dispari
# 3. Trova il Numero Massimo

numeri = [12, 3, 7, 24, 5, 18, 9, 10, 15, 2]

somma_dispari = 0
numero_massimo = numeri[0]  

for numero in numeri:
    if numero % 2 == 0:
        print("Numero pari:", numero)
    else:
        print("Numero dispari:", numero)
        somma_dispari += numero

   
    if numero > numero_massimo:
        numero_massimo = numero

print("\nSomma dei numeri dispari:", somma_dispari)
print("Numero massimo nella lista:", numero_massimo)
