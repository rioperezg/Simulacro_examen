"""""
Kevin y Stuart quieren jugar al ' The Minion Game '.
Reglas del juego
Ambos jugadores reciben la misma cadena de caracteres
Ambos jugadores tienen que hacer subcadenas usando las letras de la cadena
Stuart tiene que formar palabras que comiencen con consonantes .
Kevin tiene que formar palabras que comiencen con vocales .
El juego termina cuando ambos jugadores han creado todas las subcadenas posibles.
Puntuación
Un jugador obtiene un +1punto por cada aparición de la subcadena en la cadena.
Por ejemplo :
String= BANANA
Palabra inicial de la vocal de Kevin = ANA
Aquí, ANA aparece dos veces en BANANA . Por lo tanto, Kevin obtendrá 2puntos.
Para una mejor comprensión, vea la imagen a continuación:
• Tu tarea es determinar el ganador del juego y su puntuación. El nombre y la
puntuación del ganador, separados por un espacio en una línea, o Draw si no hay
ningún ganador
"""
def Consonantes(string):
    consonantes = list("BCDFGHJKLMNPQRSTVWXYZ")
    for i in string:
        for j in consonantes:
            if i == j:
                print(i)
def minion_game(string):
    vocales = list("AEIOU")
    consonantes = list("BCDFGHJKLMNPQRSTVWXYZ")
    for i in string:
        for j in vocales:
            if i == j:
                for k in string:
                    for l in consonantes:
                        if k == l:
                            print(i+k)
            else:
                break                

                

string1 = "BANANA"
print(minion_game(string1))

    # consonantes pertenecientes a la cadena: B, N. Vocales pertenecientes a la cadena: A 
    # Si recorremos una cadena como si fuera una lista, y comparamos con una lista de vocales, seleccionamos esas vocales 
    # y formamos subcadenas empezando por esas vocales.

"""""
  CORRECCION
"""   

    # Definimos una función que tome una cadena de caracteres y devuelva un diccionario con las subcadenas y su puntuación
def minion_game(string):
  # Creamos un diccionario vacío que almacenará las subcadenas y su puntuación
  substrings = {}
  
  # Iteramos sobre todas las letras de la cadena
  for i in range(len(string)):
    # Stuart forma palabras que comiencen con consonantes
    if string[i] not in "AEIOU":
      # Iteramos sobre todas las subcadenas que comiencen con la letra actual
      for j in range(i + 1, len(string) + 1):
        # Agregamos la subcadena al diccionario y aumentamos su puntuación en 1
        substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1
        
    # Kevin forma palabras que comiencen con vocales
    else:
      # Iteramos sobre todas las subcadenas que comiencen con la letra actual
      for j in range(i + 1, len(string) + 1):
        # Agregamos la subcadena al diccionario y aumentamos su puntuación en 1
        substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1
  return substrings
# Probamos la función con la cadena "BANANA"
minion_game("BANANA")
