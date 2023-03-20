import numpy as np
from collections import deque
import sys
import time

algorithm_type = sys.argv[1]
priority = sys.argv[2]
with open(f"puzzles/{sys.argv[3]}", "r") as f:
    rows, cols = np.fromfile(f, dtype=int, count=2, sep=" ")
    data = np.fromfile(f, dtype=int, count=rows * cols, sep=" ").reshape((rows, cols))

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
    if is_solved_v2(tuple(board)):
        return path
    if current_depth >= MAX_DEPTH:
        return None
    board_copy = board.copy()
    board_copy.append(current_depth)
    visited.add(hash(tuple(board_copy)))
    index = board.index(0)
    for move in priority:
        if move == "U" and int(index / COL) != 0:  # mozna sie ruszyc do góry   #index >= COL:
            if path == "" or path[-1] != "D":
                new_board = change_state(board, "U", index)
                board_copy = new_board.copy()
                board_copy.append(current_depth)
                if hash(tuple(board_copy)) not in visited:
                    path += "U"  # path.append("U")
                    result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                    if result is not None:
                        return result
                    path = path[:-1]  # path.pop()
        elif move == "L" and index % COL != 0:  # ruch w lewo index % COL != 0
            if path == "" or path[-1] != "R":
                new_board = change_state(board, "L", index)
                board_copy = new_board.copy()
                board_copy.append(current_depth)
                if hash(tuple(board_copy)) not in visited:
                    path += "L"
                    result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                    if result is not None:
                        return result
                    path = path[:-1]
        elif move == "D" and int(index / COL) != ROW - 1:  # ruch w dol  index < COL * ROW - COL
            if path == "" or path[-1] != "U":
                new_board = change_state(board, "D", index)
                board_copy = new_board.copy()
                board_copy.append(current_depth)
                if hash(tuple(board_copy)) not in visited:
                    path += "D"
                    result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                    if result is not None:
                        return result
                    path = path[:-1]
        elif move == "R" and index % COL != COL - 1:  # ruch w prawo  and (index + 1) % COL != 0 and index < COL * ROW - 1
            if path == "" or path[-1] != "L":
                new_board = change_state(board, "R", index)
                board_copy = new_board.copy()
                board_copy.append(current_depth)
                if hash(tuple(board_copy)) not in visited:
                    path += "R"
                    result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                    if result is not None:
                        return result
                    path = path[:-1]
    return None


def bfs_algorithm_v2(board, priority):  # tez sprawdac poprzedni ruch
    visited = set()
    q = deque([(board, "")])
    visited.add(tuple(board))

    while q:
        state, path = q.popleft()
        if is_solved_v2(tuple(state)):
            return path

        index = state.index(0)
        for move in priority:
            if move == "U" and int(index / COL) != 0:  # mozna sie ruszyc do góry
                new_board = change_state(state, "U", index)
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    q.append((new_board, path + "U"))

            elif move == "L" and index % COL != 0:  # ruch w lewo
                new_board = change_state(state, "L", index)
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    q.append((new_board, path + "L"))

            elif move == "D" and int(index / COL) != ROW - 1:  # ruch w dol
                new_board = change_state(state, "D", index)
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    q.append((new_board, path + "D"))

            elif move == "R" and index % COL != COL - 1:  # ruch w prawo
                new_board = change_state(state, "R", index)
                if tuple(new_board) not in visited:
                    visited.add(tuple(new_board))
                    q.append((new_board, path + "R"))

    return None