from visualizer import PathVisualizer
from searchers import *
import numpy as np

I = float('INF')

def main():
    matrix = np.array([
        [5, 4, 5, 6, 7, 8, 9, 10, float('inf'), 18, 19, 20],
        [4, 3, 4, 5, float('inf'), 7, 8, 9, float('inf'), 17, 18, 19],
        [3, 2, 3, 4, float('inf'), 6, 7, 8, float('inf'), 16, 17, 18],
        [2, 1, 2, 3, float('inf'), 5, 6, 7, float('inf'), 15, 16, 17],
        [1, 0, 1, 2, 3, 4, 5, 6, float('inf'), 14, 15, 16],
        [2, 1, 2, 3, 4, 5, 6, 7, float('inf'), 13, 14, 15],
        [3, 2, 3, 4, 5, 6, 7, 8, float('inf'), 12, 13, 14],
        [4, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 9, 10, 11, 12, 13],
        [5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    ])

    start = (4, 1)  # Position of 0
    end = (1, 11)   # Position of 19
    visualizer = PathVisualizer(use_colors=True)  # Activate colors

    # Test BFS
    print("\n=== BFS Search ===")
    bfs = BFSSearch(matrix)
    path_bfs, cost_bfs, explored_bfs = bfs.search(start, end)
    if path_bfs:
        print(f"Path found: {path_bfs}")
        print(f"Total cost: {cost_bfs}")
        print(f"Explored cells: {len(explored_bfs)}")
        visualizer.visualize_path(matrix, path_bfs, explored_bfs, start, end)

    # Test A*
    print("\n=== A* Search ===")
    astar = AStarSearch(matrix)
    path_astar, cost_astar, explored_astar = astar.search(start, end)
    if path_astar:
        print(f"Path found: {path_astar}")
        print(f"Total cost: {cost_astar}")
        print(f"Explored cells: {len(explored_astar)}")
        visualizer.visualize_path(matrix, path_astar, explored_astar, start, end)

if __name__ == "__main__":
    main()