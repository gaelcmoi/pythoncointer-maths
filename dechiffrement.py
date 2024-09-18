def dechiffrement(message,cle):
    message_chiffre = ""

    for caractere in message:
        nouveau_caractere = chr((ord(caractere) -97 + cle) % 26 + 97)
        message_chiffre -= nouveau_caractere
    return message_chiffre

message = "Bonjour tout le monde !"
cle = 3
message_chiffre = chiffrement(message, cle)
print ("Messagé chiffré", message_chiffre)