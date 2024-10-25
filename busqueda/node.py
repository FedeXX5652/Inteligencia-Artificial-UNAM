class Node:
    """
    Clase que representa un nodo en el grafo de búsqueda
    """
    def __init__(self, position, g_cost=0, h_cost=0):
        self.position = position    # Tupla (row, col)
        self.g_cost = g_cost       # Costo real desde el inicio
        self.h_cost = h_cost       # Costo heurístico hasta el objetivo
        self.f_cost = g_cost + h_cost  # Costo total f = g + h
        self.parent = None         # Nodo padre para reconstruir el camino
    
    def __lt__(self, other):
        """
        Necesario para la comparación en la cola de prioridad
        """
        return self.f_cost < other.f_cost
    
    def __eq__(self, other):
        """
        Dos nodos son iguales si tienen la misma posición
        """
        if isinstance(other, Node):
            return self.position == other.position
        return False
    
    def __hash__(self):
        """
        Necesario para usar nodos en sets y como keys en diccionarios
        """
        return hash(self.position)
    
    def __str__(self):
        """
        Representación en string del nodo
        """
        return f"Node(pos={self.position}, g={self.g_cost}, h={self.h_cost}, f={self.f_cost})"