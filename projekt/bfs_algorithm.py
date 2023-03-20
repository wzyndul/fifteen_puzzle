from collections import deque


class Bfs:
    def __init__(self, board):
        self.board = board
        self.visited = set()

    def bfs_solve(self):
        q = deque([(self.board, "")])
        self.visited.add(self.board.__hash__())
        while q:
            state, path = q.popleft()
            if state.is_solved():
                return path
            state.move()
            for neighbour in state.get_neighbors():
                if neighbour.__hash__() not in self.visited:
                    self.visited.add(neighbour.__hash__())
                    q.append((neighbour, path + neighbour.last_move))
        return None
