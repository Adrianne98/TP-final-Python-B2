import json
import os
save_file = 'grid_save.json'

def save_grid_to_file(grid, filename):
    """Sauvegarde la grille dans un fichier JSON."""
    with open(filename, 'w') as f:
        json.dump(grid, f)
        
def load_grid_from_file(filename):
    """Charge la grille depuis un fichier JSON."""
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        grid = json.load(f)
    return grid