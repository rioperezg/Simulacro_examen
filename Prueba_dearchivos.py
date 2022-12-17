def Minion_Game(strings):
    #Declaramos el diccionario para ir metiendo en este las subcadenas
    Substrings = {}
    #Cogemos la palabra introducida Strings y recorremos cada letra de la msima
    for i in range(len(strings)):
        #condicional de que i no pertenenzca a ninguna vocal
        if strings[i] not in ("AEIOU"):
           #Vamos con las consonantes
            for j in range(i + 1, len(strings) + 1):
                #Ahora si modificamos el diccionario antes creado
                Substrings[strings[i:j]] = Substrings.get(strings[i:j], 0) + 1
        else:
            for j in range(i + 1, len(strings) + 1):    
                Substrings[strings[i:j]] = Substrings.get(strings[i:j], 0) + 1
    return Substrings
print(Minion_Game("Stuart"))        