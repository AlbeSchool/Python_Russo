#Le liste servono a trattenere più informazioni
#Sono dei contenitori di elementi simili tra loro. Ovverro sono dei contenutori omogenei, vuol dire che il tipo di dato è sempre lo stesso. Tutte stringhe, tutti numeri, tutti boolean

#Sintassi. le parentesi [] identificano la lista
miaLista = ["mela", "pesca", "banana", "Kiwi"]
print(miaLista)

print(miaLista[1])

print(len(miaLista))


for frutto in miaLista:
    print(frutto)
#il ciclo for è adatto a stampare ogni singolo elemento della lista


#ESEMPIO, fornisco una lista di voti. Tutte le volte che è insufficiente stampo un avviso

voti = [100, 50, 25, 85, 20]

for voto in voti:
    if voto < 50:
        print("Voto: ", voto, "Attenzione sei sotto soglia di sufficienza")
    else:
        print("voto: ", voto)