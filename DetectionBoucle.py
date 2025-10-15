def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)

def detect_loop(history, current_state):
    return current_state in history

# Exemple d’utilisation :
history = []

grid1 = [[0,1,0],[0,1,0],[0,1,0]]
grid2 = [[0,0,0],[1,1,1],[0,0,0]]

state1 = grid_to_tuple(grid1)
state2 = grid_to_tuple(grid2)

# On simule l'évolution
history.append(state1)

if detect_loop(history, state2):
    print("Boucle détectée !")
else:
    print("Pas de boucle.")

history.append(state2)

if detect_loop(history, state1):
    print("Boucle détectée !")  # Ici, ça détecte
