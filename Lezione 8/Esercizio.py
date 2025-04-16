#scrivi un programma che stampa tutti i numeri da 1 a 100
#per i multiplii di 3 stampa "BOOM"
#per i multipli di 5 stampa "ZOOM"
#per i multipli di 3 e 5 stampa "Bazinga"

#esempio:
#1  
#2
#3 BOOM
#4
#5 ZOOM
#6 BOOM
#7
#8
#9 BOOM
#10 ZOOM
#11
#12 BOOM
#13
#14
#15 Bazinga

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Bazinga")
    elif i % 3 == 0:
        print("BOOM")
    elif i % 5 == 0:
        print("ZOOM")
    else:
        print(i)