#Chiffrement de César et déchiffrement brute force

#Je definis les diffrentes actions du programme dans des fonctions

def chiffrer (message, clee):

    """cette fonction chiffre le message"""

    message_chiffre = ""
    for lettres in message:
            position = alphabet.find(lettres)
            nouvelle_position = (position + clee) % 26
            nouvelle_lettre = alphabet[nouvelle_position] 
            message_chiffre = message_chiffre + nouvelle_lettre      

    return (message_chiffre)

def dechiffrer (message, clee):

    """cette fonction dechiffre un message si la clée est connue"""

    message_dechiffre = ""
    for lettres in message:
        position = alphabet.find(lettres)
        nouvelle_position = (position - clee) % 26
        nouvelle_lettre = alphabet[nouvelle_position] 
        message_dechiffre = message_dechiffre + nouvelle_lettre      
        
    return (message_dechiffre)

def brute_force (message):

    """cette focntion essaye toute les combinaisons de clées possibles pour dechiffrer le message si la clée est inconnue"""

    for clee in range(26):
         message_dechiffre = ""
         for lettres in message:
             position = alphabet.find(lettres)
             ancienne_position = (position - clee) % 26
             ancienne_lettre = alphabet[ancienne_position] 
             message_dechiffre = message_dechiffre + ancienne_lettre
         print(f"Clée{clee}: {message_dechiffre}")

    return (message_dechiffre)

# Je stock tout dans des variables et je recupère les input

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("voulez-vous (c)hiffrer ou (d)échiffer ?")
action = input ("")
message = input("entrez votre message :")
message = message.upper()

#Le programme principal qui organise les actions : chiffrer/ déchiffrer/ forcer

if action == "c":
    clee = int(input("entrez la clé : "))
    resultat = chiffrer(message, clee)
    print(resultat)
elif action == "d":
    reponse = input("connaissez vous la clée o/n ?")
    if reponse == "o":
        clee = int(input("entrez la clé : "))
        resultat = dechiffrer(message, clee)
        print(resultat)
    elif reponse =="n":
            resultat = brute_force(message)
            print(resultat)



