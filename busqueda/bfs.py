from collections import deque
from searcher import *

class BFSSearch(SearchBase):
    def search(self, start, end):
        self.explored = set()
        
        dist = [[I for _ in range(self.cols)] for _ in range(self.rows)]
        dist[start[0]][start[1]] = 0
        q = deque()
        q.append((start[0], start[1]))

        parent = {}
        parent[start] = None
        
        while q:
            current_x, current_y = q.popleft()
            current = (current_x, current_y)

            if current == end:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent.get(current)
                path = path[::-1]
                return path, self.get_path_cost(path), self.explored
            
            self.explored.add(current)

            for neighbor in self.get_neighbors(current):
                new_x, new_y = neighbor

                if dist[current_x][current_y] + self.matrix[new_x][new_y] < dist[new_x][new_y]:
                    dist[new_x][new_y] = dist[current_x][current_y] + self.matrix[new_x][new_y]
                    parent[neighbor] = current
                    q.append((new_x, new_y))
        
        return None, I, self.explored