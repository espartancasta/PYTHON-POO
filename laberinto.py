import random

# Tamaño del laberinto
width = 10
height = 10

# Crear el laberinto inicial lleno de paredes
maze = [['#'] * width for _ in range(height)]

# Direcciones (arriba, abajo, izquierda, derecha)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def generate_maze(x, y):
    maze[x][y] = ' '  # Marcar el punto actual como camino
    random.shuffle(directions)  # Mezclar las direcciones para tener un laberinto aleatorio
    
    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == '#':
            maze[x + dx][y + dy] = ' '  # Abrir camino intermedio
            generate_maze(nx, ny)  # Recursivamente generar el laberinto desde el nuevo punto

# Generar el laberinto desde una posición inicial
generate_maze(0, 0)

# Mostrar el laberinto
for row in maze:
    print(''.join(row))

# Resolver el laberinto utilizando DFS
def solve_maze(x, y, path=[]):
    if not (0 <= x < height and 0 <= y < width):
        return False  # Fuera de límites
    if maze[x][y] == '#':
        return False  # Pared
    if (x, y) in path:
        return False  # Ya visitado
    path.append((x, y))  # Añadir al camino
    
    if (x, y) == (height - 1, width - 1):  # Llegó al final
        return path  # Camino encontrado
    
    for dx, dy in directions:
        if solve_maze(x + dx, y + dy, path):
            return path
    
    path.pop()  # Eliminar el camino si no es válido
    return False

# Resolver el laberinto desde la posición inicial
solution = solve_maze(0, 0)

# Mostrar la solución del laberinto
if solution:
    solution_maze = [row.copy() for row in maze]
    for x, y in solution:
        solution_maze[x][y] = '.'
    for row in solution_maze:
        print(''.join(row))
else:
    print("No hay solución para el laberinto.")
