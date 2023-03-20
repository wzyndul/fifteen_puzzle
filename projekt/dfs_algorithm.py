class Dfs:
    def __init__(self):
        self.path = ""
        self.visited = set()
        self.max_depth = 20

    def dfs_solve(self, board):
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
                if result is not None:
                    return result
                self.path = self.path[:-1]  # path.pop()
        return None
