from queue import PriorityQueue


class Astr:
    def __init__(self, board):
        self.board = board

    def astr_solve(self):
        q = PriorityQueue()
        q.put((0, self.board))
        closed_set = set()
        while not q.empty():
            # Get the node with the lowest cost
            current = q.get()[1]
            closed_set.add(current.__hash__())

            if current.is_solved():
                path = ""
                while current.last_move != "":
                    path += current.last_move
                    current = current.parent
                reversed_path = path[::-1]
                return reversed_path

            # Loop through the neighbors of the current node
            current.move()
            for neighbor in current.get_neighbors():

                if neighbor.__hash__() not in closed_set:
                    cost = neighbor.depth + neighbor.get_heuristic_cost()
                    q.put((cost, neighbor))

        # No path found
        return None
