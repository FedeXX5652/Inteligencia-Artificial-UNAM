from collections import deque
from searcher import *

class BFSSearch(SearchBase):
    def search(self, start, end):
        self.explored = set()  # To keep track of explored nodes
        q = deque([start])  # Initialize queue with the starting node
        parent = {start: None}  # Dictionary to keep track of parent nodes for path reconstruction
        
        while q:
            current = q.popleft()  # Get the current node from the queue
            
            if current == end:  # If we've reached the goal
                path = []
                while current is not None:
                    path.append(current)  # Backtrack to construct the path
                    current = parent[current]
                path.reverse()  # Reverse to get the path from start to end
                return path, len(path) - 1, self.explored  # Return path and cost (number of edges)
            
            self.explored.add(current)  # Mark current node as explored
            
            # Get neighbors for the current node
            for neighbor in self.get_neighbors(current):
                if neighbor not in self.explored and neighbor not in q:  # Check if the neighbor has not been explored or added to the queue
                    parent[neighbor] = current  # Set the parent of the neighbor
                    q.append(neighbor)  # Add the neighbor to the queue
        
        return None, I, self.explored  # Return None if no path is found