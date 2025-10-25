def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)

def detect_loop(history_set, current_state):
    return current_state in history_set

# ✅ Exemple d’utilisation :
history = set()  # utilisation d’un set au lieu d’une liste

display_grid1 = [[0,1,0],
                 [0,1,0],
                 [0,1,0]]

display_grid2 = [[0,0,0],
                 [1,1,1],
                 [0,0,0]]

# Convertir les grilles en tuples pour pouvoir les stocker dans un set
state1 = grid_to_tuple(display_grid1)
state2 = grid_to_tuple(display_grid2)

# Simuler l'évolution
history.add(state1)


if detect_loop(history, state2):
    print("Boucle détectée !")
else:
    print("Pas de boucle.")  # ✅ Affiche ça

history.add(state2)

if detect_loop(history, state1):
    print("Boucle détectée !")  # ✅ Affiche ça aussi