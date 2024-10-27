from searcher import *
import heapq

class AStarSearch(SearchBase):
    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def search(self, start, end):
        self.explored = set()
        
        start_entry = (self.manhattan_distance(start, end), 0, start, [start])
        pq = [start_entry]

        best_costs = {start: 0}
        
        while pq:
            _, current_cost, current_pos, current_path = heapq.heappop(pq)
            
            if current_pos == end:
                return current_path, self.get_path_cost(current_path), self.explored
            
            if current_pos in self.explored:
                continue
                
            self.explored.add(current_pos)

            for neighbor in self.get_neighbors(current_pos):
                new_cost = current_cost + self.matrix[neighbor[0]][neighbor[1]]

                if neighbor not in best_costs or new_cost < best_costs[neighbor]:
                    best_costs[neighbor] = new_cost
                    f_cost = new_cost + self.manhattan_distance(neighbor, end)
                    new_path = current_path + [neighbor]
                    heapq.heappush(pq, (f_cost, new_cost, neighbor, new_path))
        
        return None, I, self.explored