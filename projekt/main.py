from queue import PriorityQueue

import numpy as np
from collections import deque
import sys
import time
from board import Board

algorithm_type = sys.argv[1]
priority = sys.argv[2]
with open(f"puzzles/{sys.argv[3]}", "r") as f:
    rows, cols = np.fromfile(f, dtype=int, count=2, sep=" ")
    data = np.fromfile(f, dtype=int, count=rows * cols, sep=" ").reshape((rows, cols))

list_puzzle = data.flatten().tolist()
ROW = rows
COL = cols
MAX_DEPTH = 20
puzzle = Board(cols, rows, list_puzzle, priority)


def dfs_algorithm(board, path, visited):
    if board.is_solved():
        return path
    if board.depth >= MAX_DEPTH:
        return None
    visited.add(board.__hash__())
    board.move()
    for neighbor in board.get_neighbors():
        if neighbor.__hash__() not in visited:
            path += neighbor.last_move  # path.append("U")
            result = dfs_algorithm(neighbor, path, visited)
            if result is not None:
                return result
            path = path[:-1]  # path.pop()
    return None


def bfs_algorithm(board):
    visited = set()
    q = deque([(board, "")])
    visited.add(board.__hash__())
    while q:
        state, path = q.popleft()
        if state.is_solved():
            return path
        state.move()
        for neighbour in state.get_neighbors():
            if neighbour.__hash__() not in visited:
                visited.add(neighbour.__hash__())
                q.append((neighbour, path + neighbour.last_move))
    return None


def a_star_algorithm(board):  # niestety tylko trzymam tylko node a nie potrzebne ruchy
    q = PriorityQueue()
    q.put((0, board))
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


algorithm_result = None
if sys.argv[1] == "dfs":

    star_time = time.time_ns()
    algorithm_result = dfs_algorithm(puzzle, "", set())
    elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
    print(round(elapsed_time, 3))
    print(algorithm_result)
elif sys.argv[1] == "bfs":

    star_time = time.time_ns()
    algorithm_result = bfs_algorithm(puzzle)
    elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
    print(round(elapsed_time, 3))
    print(algorithm_result)

elif sys.argv[1] == "astr":
    star_time = time.time_ns()
    algorithm_result = a_star_algorithm(puzzle)
    elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
    print(round(elapsed_time, 3))
    print(algorithm_result)

with open(f"{sys.argv[4]}", "w") as file:  # otwiera plik i automatycznie go zamyka jak skoncze pisac
    if algorithm_result is not None:
        file.write(f"{len(algorithm_result)}\n{algorithm_result}")
    else:
        file.write("-1")
