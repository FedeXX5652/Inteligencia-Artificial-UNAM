I = float('INF')

class SearchBase:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.explored = set()
    
    def get_neighbors(self, current):
        row, col = current
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbors = []
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < self.rows and 
                0 <= new_col < self.cols and 
                self.matrix[new_row][new_col] != I):
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def get_path_cost(self, path):
        return sum(self.matrix[row][col] for row, col in path)