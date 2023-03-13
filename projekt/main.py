import numpy as np
from collections import deque
import queue

with open("C:/studia/semestr4/SztucznaInteligencja/pietnastka/puzzles/4x4_07_00211.txt") as f:
    rows, cols = np.fromfile(f, dtype=int, count=2, sep=" ")
    data = np.fromfile(f, dtype=int, count=rows * cols, sep=" ").reshape((rows, cols))

# przepisuje do listy na potrzeby drugiego algorytmu
list_puzzle = data.flatten().tolist()
ROW = rows
COL = cols
MAX_DEPTH = 20


def is_solved_v2(board):
    solution = list(range(1, ROW * COL)) + [0]
    return board == tuple(solution)


def change_state(board, move, index):
    new_board = board.copy()
    if move == "U":
        temp = new_board[index - COL]
        new_board[index - COL] = 0
        new_board[index] = temp
        return new_board

    elif move == "D":
        temp = new_board[index + COL]
        new_board[index + COL] = 0
        new_board[index] = temp
        return new_board

    elif move == "R":
        temp = new_board[index + 1]
        new_board[index + 1] = 0
        new_board[index] = temp
        return new_board

    elif move == "L":
        temp = new_board[index - 1]
        new_board[index - 1] = 0
        new_board[index] = temp
        return new_board
    return None


def dfs_algorithm_v2(board, path, visited, current_depth, priority):
    # print(path)
    if is_solved_v2(tuple(board)):
        return path
    if current_depth >= MAX_DEPTH:
        return None
    visited.add(tuple(board))
    index = board.index(0)
    for move in priority:
        if move == "U" and index >= COL:  # mozna sie ruszyc do góry
            new_board = change_state(board, "U", index)
            if tuple(new_board) not in visited:
                path += "U"  # path.append("U")
                result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                if result is not None:
                    return result
                path = path[:-1]  # path.pop()
        elif move == "L" and index % COL != 0:  # ruch w lewo
            new_board = change_state(board, "L", index)
            if tuple(new_board) not in visited:
                path += "L"
                result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                if result is not None:
                    return result
                path = path[:-1]
        elif move == "D" and index < COL * ROW - COL:  # ruch w dol
            new_board = change_state(board, "D", index)
            if tuple(new_board) not in visited:
                path += "D"
                result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                if result is not None:
                    return result
                path = path[:-1]
        elif move == "R" and (index + 1) % COL != 0 and index < COL * ROW - 1:  # ruch w prawo
            new_board = change_state(board, "R", index)
            if tuple(new_board) not in visited:
                path += "R"
                result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                if result is not None:
                    return result
                path = path[:-1]
    return None


def bfs_algorithm(board, priority):
    visited = set()
    q = deque([(board, "")])
    visited.add(tuple(board))

    while q:
        state, path = q.popleft()
        if is_solved_v2(tuple(state)):
            return path

        index = state.index(0)
        for move in priority:
            if move == "U" and index >= COL:  # mozna sie ruszyc do góry
                new_board = change_state(state, "U", index)
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    q.append((new_board, path + "U"))

            elif move == "L" and index > 0 and index % COL != 0:  # ruch w lewo
                new_board = change_state(state, "L", index)
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    q.append((new_board, path + "L"))

            elif move == "D" and index < COL * ROW - COL:  # ruch w dol
                new_board = change_state(state, "D", index)
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    q.append((new_board, path + "D"))

            elif move == "R" and index + 1 % COL != 0 and index < COL * ROW - 1:  # ruch w prawo
                new_board = change_state(state, "R", index)
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    q.append((new_board, path + "R"))

    return None


# def Astr(board, heuristic):
#     q = queue.PriorityQueue()



priority = ["U", "L", "D", "R"]
dfs_result = dfs_algorithm_v2(list_puzzle, "", set(), 0, priority)
print(dfs_result)


# bfs_result = bfs_algorithm(list_puzzle, priority)
# print(bfs_result)

#TODO rozbić na wiele plików i klas   klasa boarda, solver(ma metode bfs i dfs)
#TODO ogarnac zapisywanie do plików i wywoływanie programu