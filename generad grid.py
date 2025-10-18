import display_grid
import DetectionBoucle
def grid():
    min_size = 5
    max_size = 63
    rows = int(display_grid.input_rows)
    columns = int(display_grid.input_columns)


    if rows < min_size or rows > max_size or columns < min_size or columns > max_size:
        print(f"Error: Grid size must be between {min_size} and {max_size}.")
        return []
    return [[0 for _ in range(columns)] for _ in range(rows)]

    
for row in grid():

    print(row)
print("Grid created successfully!") if grid() else print("Failed to create grid.")