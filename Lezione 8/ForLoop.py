#In precedenza con il while
# i = 0
# while i < 100:
#     print(i)
#     i += 1

#Con il ciclo for non sono nei cicli indefiniti, ma nei cicli definiti.
#Dobbiamo usare anche un metodo chiamato range(numero) il quale definisce il numero di cicli da effettuare

#i sta per indice
for i in range(10):
    print(i)

for i in range(15, 20):
    print("La i vale", i)

for i in range(5, 60 , 3):
    print("La i vale", i)


#Break e Continue
#Break permette di interrompere un ciclo
#Continue permette di saltare un ciclo

#Esempio : dato un set di numeri da 1 a 10 interrompi il ciclo de incontri il numero 5

for x in range(1, 11):
    if x == 5:
        break

    print("la x vale", x)

#dato un set di numeri da 1 a 10 quando incontri il numero 5 salta quel ciclo

for x in range(1, 11):
    if x == 5:
        continue

    print("la x vale", x)

    for parola in range(0,101):
        print("giorgia")