#Chiffrement de César et déchiffrement brute force

#Je definis les diffrentes actions du programme dans des fonctions qui seront utilisées dans le programme principal. 

def chiffrer (message, cle):

    """cette fonction chiffre le message"""

    message_chiffre = ""
    for lettres in message:
            position = alphabet.find(lettres)
            nouvelle_position = (position + cle) % 26
            nouvelle_lettre = alphabet[nouvelle_position] 
            message_chiffre = message_chiffre + nouvelle_lettre      

    return (message_chiffre)

def dechiffrer (message, cle):

    """cette fonction dechiffre un message si la clé est connue"""

    message_dechiffre = ""
    for lettres in message:
        position = alphabet.find(lettres)
        nouvelle_position = (position - cle) % 26
        nouvelle_lettre = alphabet[nouvelle_position] 
        message_dechiffre = message_dechiffre + nouvelle_lettre      
        
    return (message_dechiffre)

def brute_force (message):

    """cette focntion essaye toute les combinaisons de clés possibles pour dechiffrer le message si la clé est inconnue"""

    for cle in range(26):
         message_dechiffre = ""
         for lettres in message:
             position = alphabet.find(lettres)
             ancienne_position = (position - cle) % 26
             ancienne_lettre = alphabet[ancienne_position] 
             message_dechiffre = message_dechiffre + ancienne_lettre
         print(f"Clée{cle}: {message_dechiffre}")

    return (message_dechiffre)

# Je met l'alphabet et les print, je recupère les input et les stocke dans des variables.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("voulez-vous (c)hiffrer ou (d)échiffer ?")
action = input ("")
message = input("entrez votre message :")
message = message.upper()

#Le programme principal qui fait appel aux actions : chiffrer/ déchiffrer/ forcer. 

if action == "c":
    cle = int(input("entrez la clé : "))
    resultat = chiffrer(message, cle)
    print(resultat)
elif action == "d":
    reponse = input("connaissez vous la clée o/n ?")
    if reponse == "o":
        cle = int(input("entrez la clé : "))
        resultat = dechiffrer(message, cle)
        print(resultat)
    elif reponse =="n":
            resultat = brute_force(message)
            print(resultat)



