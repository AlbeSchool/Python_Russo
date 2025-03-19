print("Ciao! come ti chiami")

nome = input()

print("Ciao", nome,"Quanto desideri depositare?")

deposito = int(input())

saldo = 0

saldo += deposito

if deposito > 600:
    print("Non puoi depositare più di €600")
