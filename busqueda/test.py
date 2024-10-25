import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import heapq

# Define the grid
matrix = np.array([
    [5, 4, 5, 6, 7, 8, 9, 10, float('INF'), 18, 19, 20],
    [4, 3, 4, 5, float('INF'), 7, 8, 9, float('INF'), 17, 18, 19],
    [3, 2, 3, 4, float('INF'), 6, 7, 8, float('INF'), 16, 17, 18],
    [2, 1, 2, 3, float('INF'), 5, 6, 7, float('INF'), 15, 16, 17],
    [1, 0, 1, 2, 3, 4, 5, 6, float('INF'), 14, 15, 16],
    [2, 1, 2, 3, 4, 5, 6, 7, float('INF'), 13, 14, 15],
    [3, 2, 3, 4, 5, 6, 7, 8, float('INF'), 12, 13, 14],
    [4, float('INF'), float('INF'), float('INF'), float('INF'), float('INF'), float('INF'), 9, 10, 11, 12, 13],
    [5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
])

start = (4, 1)  # Starting point (row, column)
end = (1, 11)   # Ending point (row, column)

def bfs(matrix, start, end):
    rows, cols = matrix.shape
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.popleft()
        
        if current == end:
            break

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                neighbor not in visited and matrix[neighbor] != float('INF')):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    
    path = []
    if current == end:
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
    
    return path, visited

def a_star(matrix, start, end):
    rows, cols = matrix.shape
    open_set = []
    heapq.heappush(open_set, (0, start))
    g_costs = {start: 0}
    f_costs = {start: heuristic(start, end)}
    visited = set()
    parent = {start: None}

    while open_set:
        current = heapq.heappop(open_set)[1]
        visited.add(current)

        if current == end:
            break

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                matrix[neighbor] != float('INF')):
                
                tentative_g_cost = g_costs[current] + matrix[neighbor]

                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_costs[neighbor] = tentative_g_cost + heuristic(neighbor, end)
                    parent[neighbor] = current

                    if neighbor not in visited:
                        heapq.heappush(open_set, (f_costs[neighbor], neighbor))

    path = []
    if current == end:
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()

    return path, visited

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def plot_grid(matrix, path, visited, title):
    plt.imshow(matrix, cmap='hot', interpolation='nearest', vmin=0, vmax=20)
    for (x, y) in path:
        plt.text(y, x, 'P', ha='center', va='center', color='blue')  # Path marker
    for (x, y) in visited:
        if (x, y) not in path:
            plt.text(y, x, 'V', ha='center', va='center', color='cyan')  # Visited marker

    plt.title(title)
    plt.colorbar()
    plt.grid(False)

# Run BFS and A*
bfs_path, bfs_visited = bfs(matrix, start, end)
a_star_path, a_star_visited = a_star(matrix, start, end)

# Print paths
print("BFS Path:", bfs_path)
print("A* Path:", a_star_path)

# Create subplots for BFS and A*
plt.figure(figsize=(12, 6))

# Plot BFS
plt.subplot(1, 2, 1)
plot_grid(matrix, bfs_path, bfs_visited, 'BFS Path')

# Plot A*
plt.subplot(1, 2, 2)
plot_grid(matrix, a_star_path, a_star_visited, 'A* Path')

plt.tight_layout()
plt.show()