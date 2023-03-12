import numpy as np
from collections import deque

with open("C:/studia/semestr4/SztucznaInteligencja/pietnastka/puzzles/4x4_07_00211.txt") as f:
    rows, cols = np.fromfile(f, dtype=int, count=2, sep=" ")
    data = np.fromfile(f, dtype=int, count=rows * cols, sep=" ").reshape((rows, cols))

# przepisuje do listy na potrzeby drugiego algorytmu
lista_ukladanka = data.flatten().tolist()
ROW = rows
COL = cols


def is_solved_v2(board):
    solution = list(range(1, ROW * COL)) + [0]
    return board == solution


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


def dfs_algorithm_v2(board, path, visited, current_depth, max_depth):
    print(path)
    if is_solved_v2(board):
        return path
    if current_depth >= max_depth:
        return None
    visited.add(tuple(board))
    index = board.index(0)
    if index >= COL:  # mozna sie ruszyc do góry
        new_board = change_state(board, "U", index)
        if tuple(new_board) not in visited:
            path.append("U")
            result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, max_depth)
            if result is not None:
                return result
            path.pop()
    if index > 0 and index % COL != 0:  # ruch w lewo
        new_board = change_state(board, "L", index)
        if tuple(new_board) not in visited:
            path.append("L")
            result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, max_depth)
            if result is not None:
                return result
            path.pop()
    if index < COL * ROW - COL:  # ruch w dol
        new_board = change_state(board, "D", index)
        if tuple(new_board) not in visited:
            path.append("D")
            result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, max_depth)
            if result is not None:
                return result
            path.pop()
    if index + 1 % COL != 0 and index < COL * ROW - 1:  # ruch w prawo
        new_board = change_state(board, "R", index)
        if tuple(new_board) not in visited:
            path.append("R")
            result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, max_depth)
            if result is not None:
                return result
            path.pop()
    return None



# def bfs_algorithm(board):
#     visited = set()
#     q = deque([(board, [])])
#     visited.add(tuple(board))
#
#     while q:
#         state, path = q.popleft()
#         if is_solved_v2(state):
#             return path
#
#         index = state.index(0)
#
#         if index >= COL:  # mozna sie ruszyc do góry
#             new_board = change_state(state, "U", index)
#             if tuple(new_board) not in visited:
#                 visited.add(tuple(new_board))
#                 q.append((new_board, path + ["U"]))
#
#         if index > 0 and index % COL != 0:  # ruch w lewo
#             new_board = change_state(state, "L", index)
#             if tuple(new_board) not in visited:
#                 visited.add(tuple(new_board))
#                 q.append((new_board, path + ["L"]))
#
#         if index < COL * ROW - COL:  # ruch w dol
#             new_board = change_state(state, "D", index)
#             if tuple(new_board) not in visited:
#                 visited.add(tuple(new_board))
#                 q.append((new_board, path + ["D"]))
#
#         if index + 1 % COL != 0 and index < COL * ROW - 1:  # ruch w prawo
#             new_board = change_state(state, "R", index)
#             if tuple(new_board) not in visited:
#                 visited.add(tuple(new_board))
#                 q.append((new_board, path + ["R"]))
#
#     return None


my_set = set()
solution_path = []
xd = dfs_algorithm_v2(lista_ukladanka, solution_path, my_set, 0, 20)
print(xd)


# ok = bfs_algorithm(lista_ukladanka)
# print("okokok")
# print(ok)
