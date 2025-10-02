print("Welcome to la Vie de Conway")
print("Press size grid to continue...")
input_ligne = input("Enter number of rows: ")
input_colonne = input("Enter number of columns: ")
def grid():
    raw = int(input_ligne)
    columns = int(input_colonne)
    return [[0 for _ in range(columns)] for _ in range(raw)]
print(grid())

