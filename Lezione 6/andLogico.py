# L' AND logico oppure (&&) mi permette di unire più condizioni. VUol dire che ho bisogno che entrambe le condizioni siano valide affinché tutta la condizione sia true

#stefan compe 18, da oggi può accedere al club dei programmatori ma deve avere un invito

input("Ciao, come ti chiami? ")
età = int(input("Quanti anni hai? ")) #typecasting
invito = bool(input("Hai l'invito per il club dei programmatori? "))




if età >= 18 and invito:
    print("Ciao Stefan, puoi far parte del club dei programmatori")
elif età < 18 and invito:
    print("Ciao Stefan, non hai ancora compiuto 18 anni. anche se hai l'invito non puoi entrare")
elif età >= 18 and not invito:
    print("Ciao Stefan, non hai l'invito, non puoi far parte del club")
else:
    print("Ciao Stefan, non puoi far parte del club")
