"""""
HackerChess es una variante del ajedrez que se juega en la UAX. Es un juego que se juega entre
dos jugadores que realizan movimientos por turnos hasta que uno de ellos no puede realizar
ningún movimiento. El jugador que no puede hacer un movimiento pierde el juego y el otro
jugador es declarado ganador. El juego se juega en un tablero con filas N y N columnas.
Las únicas piezas que se utilizan en el juego son las torres. Una torre en HackerChess se mueve
solo verticalmente, lo que significa que nunca deja una columna a la que pertenece. Además,
en un solo movimiento, una torre atraviesa cualquier número de casillas desocupadas.
Tenga en cuenta que no hay capturas en HackerChess, dos torres no pueden ocupar la misma
celda y una torre no puede saltar sobre otra torre. Cada jugador tiene exactamente una torre
en cada una de las columnas del tablero.
Dada la posición inicial de las torres y sabiendo que el segundo jugador hace el primer
movimiento, decide quién ganará el juego si ambos jugadores juegan de manera óptima.
Formato de entrada
En la primera línea, hay un solo entero T que denota el número de juegos a jugar. Después de
eso, descripciones de T los juegos siguen:
En la primera línea, hay un solo entero N que denota el tamaño del tablero. Después siguen las
N líneas.
En el i-th de ellos hay un solo entero r1i que denota la fila de la torre que pertenece al primer
jugador colocado en la i-ésima columna. Después de eso, otro siguen las n líneas.
En el i-th de ellos hay un solo entero r2i que denota la fila de la torre que pertenece al segundo
jugador colocado en el i-ésima columna.
Restricciones
Formato de salida
Imprimir exactamente t-líneas. En eli -th de ellos, imprima player-1si el primer jugador gana eli-ésimo juego. De lo contrario, imprima player-2en esta línea.
"""
def verticalRooks(r1, r2):
 # Write your code here

 
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        r1 = []
        for _ in range(n):
            r1_item = int(input().strip())
            r1.append(r1_item)
            r2 = []
            for _ in range(n):
                r2_item = int(input().strip())
                r2.append(r2_item)
                result = verticalRooks(r1, r2)
print(verticalRooks(5, 5))

"""
CORRECCION
"""

N = int(input())
pos1 = []
pos2 = []
for i in range(N):
    r1, r2 = map(int, input().split())
    pos1.append(r1)
    pos2.append(r2)
# Determinar si el segundo jugador tiene la ventaja inicial
has_advantage = False
for i in range(N):
    # Si la torre del segundo jugador puede moverse en su primer movimiento,
    # el segundo jugador tiene la ventaja
    if pos2[i] < pos1[i]:
        has_advantage = True
        break
# Si el segundo jugador tiene la ventaja, debe elegir la jugada óptima
# para ganar el juego
if has_advantage:
    # Elegir la columna en la que la torre del segundo jugador esté
    # más abajo que la del primer jugador
    best_move = -1
    max_diff = -1
    for i in range(N):
        diff = pos1[i] - pos2[i]
        if diff > max_diff:
            max_diff = diff
            best_move = i
    # Mover la torre del segundo jugador a la fila más alta posible
    pos2[best_move] = N
    # Imprimir la posición actual de las torres
    for i in range(N):
        print(pos1[i], pos2[i])
else:
    # Si el primer jugador tiene la ventaja, debe elegir la jugada óptima
    # para ganar el juego
    # Elegir la columna en la que la torre del primer jugador esté
    # más abajo que la del segundo jugador
    best_move = -1
    max_diff = -1
    for i in range(N):
        diff = pos2[i] - pos1[i]
        if diff > max_diff:
            max_diff = diff
            best_move = i
    # Mover la torre del primer jugador a la fila más alta posible
    pos1[best_move] = N
    # Imprimir la posición actual de las torres
    for i in range(N):
        print(pos1[i], pos2[i])


