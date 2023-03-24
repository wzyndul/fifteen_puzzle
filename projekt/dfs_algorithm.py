class Dfs:

    def __init__(self):
        self.path = ""
        self.visited = set()
        self.max_depth = 20
        self.visited_states = 0
        self.proceesed_states = 0

    def dfs_solve(self, board):  # moze zrobic tak zeby dla dfs_a kopiowac tylko boarda, a nie cale obiekty
        if board.is_solved():
            return self.path
        if board.depth >= self.max_depth:
            return None
        self.visited.add(board.__hash__())
        board.move()
        for neighbor in board.get_neighbors():

            if neighbor.__hash__() not in self.visited:
                self.path += neighbor.last_move  # path.append("U")
                result = self.dfs_solve(neighbor)
                self.visited_states += 1
                if result is not None:
                    return result
                self.path = self.path[:-1]  # path.pop()
                self.proceesed_states += 1
        return None

    def states_counter(self):
        return self.visited_states , self.proceesed_states
