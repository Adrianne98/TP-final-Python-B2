import random
import display_grid
import DetectionBoucle
import time
import save
import os

previous_states = set()
SAVE_PATH = save.save_file  # data save JSON

#  creation grid and initialize cells
def create_grid(rows, cols):
    
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

#  Calcul cell nombers a live
def count_live_neighbors(grid, row, col):
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1),  (1,0), (1,1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            count += grid[r][c]
    return count

# update grid for next generation
def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            neighbors = count_live_neighbors(grid, r, c)
            if neighbors == 3:
                new_grid[r][c] = 1  # la cellule devient vivante
            elif neighbors == 2:
                new_grid[r][c] = grid[r][c]  # elle garde son état
            else:
                new_grid[r][c] = 0  # elle meurt
    return new_grid

if __name__ == "__main__":
#  reucpération size grid input
    rows = display_grid.input_rows
    cols = display_grid.input_columns

    # Vérification data save history
    if os.path.exists(SAVE_PATH):
        print(f"Une sauvegarde a été trouvée : {SAVE_PATH}")
        choice = input("Souhaitez-vous reprendre la partie précédente ? (o/n) : ").strip().lower()

        if choice == 'o':
            grid = save.load_grid_from_file(SAVE_PATH)
            if grid is None:
                print(" Erreur de lecture de la sauvegarde. Création d'une nouvelle grille.")
                grid = create_grid(rows, cols)
            else:
                print("Grille chargée avec succès depuis la sauvegarde.")
        else:
            print(" Réinitialisation de la simulation...")
            os.remove(SAVE_PATH)
            grid = create_grid(rows, cols)
    else:
        print(" Aucune sauvegarde trouvée. Création d'une nouvelle grille.")
        grid = create_grid(rows, cols)

    print("\nGrille initiale :")
    for row in grid:
        print(row)

    # Boucle simulation
    while True:
        state = DetectionBoucle.grid_to_tuple(grid)

        if DetectionBoucle.detect_loop(previous_states, state):
            print("boucle détectée. Arrêt du programme.")
            break

        previous_states.add(state)

        print("\nNouvelle itération :")
        for row in grid:
            print(row)

        # update generation grid
        grid = next_generation(grid)

        #  Save new grid generated
        try:
            save.save_grid_to_file(grid, SAVE_PATH)
            print(f" Grille sauvegardée dans {SAVE_PATH}")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")

        time.sleep(1.5)  # time delay between generations