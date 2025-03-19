print("ciao come ti chiami?")
nome = input()


print("ciao", nome, "preferitesti fare un prelievo o un deposito?")



saldo = 1000


risposta = input()
if risposta == "prelievo" or risposta == "Prelievo" or risposta == "PRELIEVO":
    print("quanto desideri prelevare?")
    prelievo = int(input())
    if prelievo > saldo:
        print("Non hai abbastanza soldi")
    else:
        saldo -= prelievo
        print("hai prelevato €", prelievo, "e il tuo saldo è di €", saldo)

if risposta == "deposito" or risposta == "Deposito" or risposta == "DEPOSITO":
    print("quanto desideri depositare?")
    deposito = int(input())
    if deposito < 0:
        print("Errore, non puoi depositare un valore negativo")  
    else:
        saldo += deposito
        print("hai depositato €", deposito, "e il tuo saldo è di €", saldo)