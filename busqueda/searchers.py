from node import Node

I = float('INF')

# search_base.py
class SearchBase:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.explored = set()  # Nuevo: conjunto para rastrear celdas exploradas
    
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

# bfs_search.py
from collections import deque

class BFSSearch(SearchBase):
    def search(self, start, end):
        """Implementación de Búsqueda a Ciegas - BFS"""
        self.explored = set()  # Reinicia exploradas
        queue = deque([(start, [start])])  # La cola almacena el nodo y el camino hasta el nodo
        
        while queue:
            current, path = queue.popleft()
            
            if current == end:
                return path, self.get_path_cost(path), self.explored  # Retornar cuando encontramos el final
            
            for neighbor in self.get_neighbors(current):  # Obtener vecinos válidos
                if neighbor not in self.explored:
                    self.explored.add(neighbor)  # Marcar como explorado al añadir a la cola
                    queue.append((neighbor, path + [neighbor]))  # Añadir nuevo camino a la cola
        
        return None, I, self.explored  # Si no se encuentra el camino
# astar_search.py
import heapq

class AStarSearch(SearchBase):
    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])  # Distancia Manhattan entre dos puntos
    
    def search(self, start, end):
        """Implementación de A* con heurística Manhattan"""
        self.explored = set()  # Reinicia exploradas
        start_node = Node(start)  # Nodo inicial
        open_list = [start_node]  # Lista de nodos abiertos
        closed_set = set()  # Lista de nodos cerrados
        
        while open_list:
            current = heapq.heappop(open_list)  # Obtiene el nodo con menor f_cost
            
            if current.position == end:
                path = []
                node = current
                while node:  # Reconstrucción del camino desde el nodo final al inicio
                    path.append(node.position)
                    node = node.parent
                path = path[::-1]  # Invertir para obtener el camino desde el inicio
                return path, self.get_path_cost(path), self.explored
            
            closed_set.add(current.position)  # Añadir a cerrados
            
            for neighbor_pos in self.get_neighbors(current.position):  # Revisar vecinos
                if neighbor_pos in closed_set:
                    continue  # Si ya ha sido visitado, lo ignoramos
                
                g_cost = current.g_cost + self.matrix[neighbor_pos[0]][neighbor_pos[1]]  # Costo g (real)
                h_cost = self.manhattan_distance(neighbor_pos, end)  # Costo h (heurístico)
                
                # Crear nodo vecino y establecer el nodo actual como padre
                neighbor = Node(neighbor_pos, g_cost, h_cost)  
                neighbor.parent = current
                
                # Si el nodo ya está en la lista abierta con menor f_cost, lo saltamos
                skip = False
                for node in open_list:
                    if node.position == neighbor_pos and node.f_cost <= neighbor.f_cost:
                        skip = True
                        break
                
                if not skip:  # Si no se debe saltar, lo añadimos a la lista abierta
                    heapq.heappush(open_list, neighbor)
                    self.explored.add(neighbor_pos)  # Marcar como explorado
        
        return None, I, self.explored  # Si no se encuentra el camino