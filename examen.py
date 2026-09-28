# sudoku_solver.py

def es_valido(tablero, fila, col, num):
    """Verifica si es válido colocar un número en una casilla determinada."""
    # Verificar fila
    for x in range(9):
        if tablero[fila][x] == num:
            return False

    # Verificar columna
    for x in range(9):
        if tablero[x][col] == num:
            return False

    # Verificar subcuadrícula 3x3
    inicio_fila = fila - fila % 3
    inicio_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if tablero[i + inicio_fila][j + inicio_col] == num:
                return False

    return True

def resolver_sudoku(tablero):
    """Resuelve el Sudoku mediante Backtracking."""
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][col] = 0
                return False
    return True

def imprimir_tablero(tablero):
    """Imprime el tablero de Sudoku con un formato claro."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")

# Tablero inicial extraído de la imagen del examen (0 representa casillas vacías)
tablero_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if __name__ == "__main__":
    print("=== INSTRUCCIONES DE USO ===")
    print("1. Ejecuta el script desde tu terminal con: python sudoku_solver.py")
    print("2. El programa mostrará el tablero inicial y posteriormente la solución completada.\n")
    
    print("--- Tablero Inicial ---")
    imprimir_tablero(tablero_sudoku)
    print("\nResolviendo Sudoku...\n")
    
    if resolver_sudoku(tablero_sudoku):
        print("--- Tablero Resuelto ---")
        imprimir_tablero(tablero_sudoku)
    else:
        print("No existe solución para este Sudoku.")