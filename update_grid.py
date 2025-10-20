import random
import display_grid
import DetectionBoucle
import generad_grid

# 🔸 Création de la grille initiale avec des cellules aléatoires (vivantes = 1, mortes = 0)
def create_grid(rows, cols):
    """Crée une grille rows x cols avec des cellules aléatoirement vivantes ou mortes."""
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# 🔸 Compter les voisins vivants autour d'une cellule
def count_live_neighbors(grid, row, col):
    """Compte les 8 voisins vivants autour d'une cellule donnée."""
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1),  (1,0), (1,1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            count += grid[r][c]
    return count

# 🔸 Met à jour la grille selon les règles du jeu de la vie
def next_generation(grid):
    """Retourne la grille mise à jour selon les règles de Conway."""
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

# 🔹 Exemple d'utilisation
if __name__ == "__main__":
    # Récupérer la taille depuis display_grid.py
    rows = display_grid.input_rows
    cols = display_grid.input_columns

    # Créer la grille de départ
    grid = create_grid(rows, cols)

    print("Grille initiale :")
    for row in grid:
        print(row)

    # Calculer la nouvelle génération
    new_grid = next_generation(grid)

    print("\nNouvelle génération :")
    for row in new_grid:
        print(row)