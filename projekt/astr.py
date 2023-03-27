import time
from queue import PriorityQueue


class Astr:
    def __init__(self, board):
        self.board = board
        self.visited_states = 0
        self.processed_states = 0
        self.elapsed_time = 0
        self.max_recursion_reached = 0

    def astr_solve(self):
        star_time = time.time_ns()
        q = PriorityQueue()
        q.put((0, self.board))  # wkladamy kosz i dany stan
        closed_set = set()
        while not q.empty():
            current = q.get()[1]  # biore wezel z najnizszym kosztem
            if current.depth >= self.max_recursion_reached:
                self.max_recursion_reached = current.depth

            self.processed_states += 1
            closed_set.add(current.__hash__())

            if current.is_solved():
                path = ""
                while current.last_move != "":  # cofamy sie po rodzicach do korzenia
                    path += current.last_move
                    current = current.parent
                reversed_path = path[::-1]  # odwracamy sciezke
                self.elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
                return reversed_path

            current.move()
            for neighbor in current.get_neighbors():
                self.visited_states += 1
                if neighbor.__hash__() not in closed_set:  # jesli dany stan nie byl jeszcze przetworzony
                    cost = neighbor.depth + neighbor.get_heuristic_cost()
                    q.put((cost, neighbor))

        self.elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
        return None

    def states_counter(self):
        return self.visited_states, self.processed_states

    def algorithm_time(self):
        return round(self.elapsed_time, 3)

    def recursion_reached(self):
        return self.max_recursion_reached
