#Chiffrement de César et déchiffrement brute force

#Je definis les diffrentes actions du programme dans des fonctions qui seront utilisées dans le programme principal. 

def chiffrer (message, cle):

    """cette fonction chiffre le message"""

    message_chiffre = ""
    for lettres in message:
        position = alphabet.find(lettres) #Le alphabet.find(lettres) retourne un -1 quand il ne trouve pas la lettre en question (espaces et ponctuations).
        if alphabet.find(lettres) != -1:  #On fait d'abord pour les lettres que le .find() trouve et donc ne retourne pas -1. 
            nouvelle_position = (position + cle) % 26
            nouvelle_lettre = alphabet[nouvelle_position] 
        elif alphabet.find(lettres) == -1:#Puis si il ne trouve pas, donc retourne -1 on laisse tel quel.
            nouvelle_lettre = lettres
        message_chiffre = message_chiffre + nouvelle_lettre 
    print(message_chiffre)     

    return (message_chiffre)

def dechiffrer (message, cle):

    """cette fonction dechiffre un message si la clé est connue"""

    message_dechiffre = ""
    for lettres in message:
        position = alphabet.find(lettres)
        if alphabet.find(lettres) != -1:
            nouvelle_position = (position - cle) % 26
            nouvelle_lettre = alphabet[nouvelle_position] 
        elif alphabet.find(lettres) == -1:
            nouvelle_lettre = lettres
        message_dechiffre = message_dechiffre + nouvelle_lettre
    print(message_dechiffre)      
        
    return (message_dechiffre)

def brute_force (message):

    """cette focntion essaye toute les combinaisons de clés possibles pour dechiffrer le message si la clé est inconnue"""
    
    for cle in range(26):
        message_dechiffre = ""
        for lettres in message:
            position = alphabet.find(lettres)
            if alphabet.find(lettres) != -1:  
                ancienne_position = (position - cle) % 26
                ancienne_lettre = alphabet[ancienne_position] 
            elif alphabet.find(lettres) == -1: 
                ancienne_lettre = lettres
            message_dechiffre = message_dechiffre + ancienne_lettre
        print(f"Clé{cle}: {message_dechiffre}")

    return (message_dechiffre)

# Je met l'alphabet et les print, je recupère les input et les stocke dans des variables.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("voulez-vous (c)hiffrer ou (d)échiffer ?")
action = input ("")
message = input("entrez votre message :")
message = message.upper()

#Le programme principal qui fait appel aux fonctions : chiffrer/ déchiffrer/ forcer. 

if action == "c":
    cle = int(input("entrez la clé : "))
    chiffrer(message, cle)
elif action == "d":
    reponse = input("connaissez vous la clée o/n ?")
    if reponse == "o":
        cle = int(input("entrez la clé : "))
        dechiffrer(message, cle)
    elif reponse =="n":
            brute_force(message)
            



