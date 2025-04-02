# Con i loop go la possibilità di ripetere dei blocchi di codice

#LOOP INDEFINITI: sono dei loop che potrebbero ciclare all'infinito

# SINTASSI :while condizioneTrue:
#           #fai qualcosa()

#fin tanto che la condizione è true continua ad eseguire il codice

#ATTENZIONE: un loop del genere è un loop infinito  
# while True:
#   print("Ciao") 


numStop = 0

while numStop < 10:
    numStop += 1
    print("Adesso il numero cale: ", numStop)
    
#  Esempio pratico
num_enorme = -9999999999

numero = int(input("Inserisci un numero oppure digita -1 per fermare il loop"))

while numero != -1:
    if numero > num_enorme:
        num_enorme = numero
    numero = int(input("Inserisci un numero oppure digita -1 per fermare il loop"))
    
print("Il numero più grande è: ", num_enorme)