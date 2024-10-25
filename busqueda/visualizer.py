import matplotlib.pyplot as plt
import numpy as np

class PathVisualizer:
    def __init__(self, use_colors=True):
        """
        Initializes the visualizer with the option to use colors.
        :param use_colors: Activate or deactivate colors.
        """
        self.use_colors = use_colors

    def visualize_path(self, matrix, path, explored, start, end):
        """
        Visualizes the path found and the explored cells on a grid using Matplotlib.
        :param matrix: The matrix to visualize.
        :param path: The path found.
        :param explored: The cells explored.
        :param start: The start position.
        :param end: The end position.
        """
        plt.figure(figsize=(10, 8))
        rows, cols = len(matrix), len(matrix[0])

        # Create a color grid
        color_grid = np.ones((rows, cols, 3))  # Initialize a grid with white (1, 1, 1)

        # Define colors
        visited_color = [0.5, 0.5, 0.5]  # Gray for explored cells
        path_color = [1, 1, 0]            # Yellow for path
        start_color = [0, 1, 0]           # Green for start
        end_color = [1, 0, 0]             # Red for end
        obstacle_color = [0, 0, 0]        # Black for obstacles

        # Fill colors based on cell type
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float('inf'):
                    color_grid[i, j] = obstacle_color  # Color obstacles in black
                elif (i, j) in path:
                    color_grid[i, j] = path_color  # Color path in yellow
                    if (i, j) == start:
                        color_grid[i, j] = start_color  # Color start in green
                    elif (i, j) == end:
                        color_grid[i, j] = end_color  # Color end in red
                elif (i, j) in explored:
                    color_grid[i, j] = visited_color  # Color explored cells in gray

        # Create the plot
        plt.imshow(color_grid, interpolation='nearest', aspect='auto')

        # Add numbers to cells
        for i in range(rows):
            for j in range(cols):
                cell_value = matrix[i][j]
                if cell_value != float('inf'):
                    plt.text(j, i, str(cell_value), ha='center', va='center', color='black')

        # Add a legend outside the grid
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=10, label='Explored'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', markersize=10, label='Path'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Start'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='End'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=10, label='Obstacle'),
        ]
        plt.legend(handles=legend_elements, loc='upper right', fontsize=10, bbox_to_anchor=(1.1, 1))

        plt.title('Pathfinding Visualization')
        plt.axis('off')  # Hide axis
        plt.show()
