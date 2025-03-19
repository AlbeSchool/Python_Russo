print("Anche prin è una funzione built-in")

print("insericsci il tuo nome")
nome = input()

print("ciao", nome)

saldo = 1000

print("Quanto desideri prelevare?")
prelievo = int(input()) #sto forzando l'input ad essere un intero (cast del dato)
if prelievo > saldo:
    print("Non hai abbastanza soldi")
else:
    saldo -= prelievo    
print("il tuo saldo è di €", saldo)

print("Quanto desideri depositare?")

deposito = int(input())

saldo += deposito

if deposito == 0:
    print("Non hai depositato nulla")   
else:
    print("Hai depositato €", deposito, "e il tuo saldo è di €", saldo)

if deposito < 0:
    print("Errore, non puoi depositare un valore negativo")
else:
    print("Hai depositato €", deposito, "e il tuo saldo è di €", saldo)


