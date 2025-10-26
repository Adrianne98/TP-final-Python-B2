def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)

def detect_loop(history_set, current_state):
    return current_state in history_set

history = set()  

display_grid1 = [[0,1,0],
                 [0,1,0],
                 [0,1,0]]

display_grid2 = [[0,0,0],
                 [1,1,1],
                 [0,0,0]]

state1 = grid_to_tuple(display_grid1)
state2 = grid_to_tuple(display_grid2)


history.add(state1)


if detect_loop(history, state2):
    print("Boucle détectée !")
else:
    print("Pas de boucle.") 
history.add(state2)

if detect_loop(history, state1):
    print("Boucle détectée !")  