import time


class Dfs:

    def __init__(self):
        self.path = ""
        self.visited = {}
        self.max_depth = 20
        self.visited_states = 1
        self.processed_states = 0
        self.elapsed_time = 0
        self.max_recursion_reached = 0

    def dfs_solve(self, board):
        star_time = time.time_ns()
        result = self.dfs_start(board)
        self.elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
        return result

    def dfs_start(self, board):  # moze zrobic tak zeby dla dfs_a kopiowac tylko boarda, a nie cale obiekty

        self.processed_states += 1
        if board.depth > self.max_depth:
            return None
        if board.depth >= self.max_recursion_reached:
            self.max_recursion_reached = board.depth

        if board.is_solved():
            return self.path

        self.visited[board.__hash__()] = board.depth
        board.move()
        for neighbor in board.get_neighbors():
            self.visited_states += 1
            if (neighbor.__hash__() in self.visited and neighbor.depth < self.visited[neighbor.__hash__()]) or neighbor.__hash__() not in self.visited:
                self.path += neighbor.last_move
                result = self.dfs_solve(neighbor)
                if result is not None:
                    return result
                self.path = self.path[:-1]
        return None

    def states_counter(self):
        return self.visited_states, self.processed_states

    def algorithm_time(self):
        return round(self.elapsed_time, 3)

    def recursion_reached(self):
        return self.max_recursion_reached
