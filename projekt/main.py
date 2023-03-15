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


def manhattan_heuristic(board):
    distance = 0
    for x in range(0, ROW):
        for y in range(0, COL):
            board_value = board[x * ROW + y]  # wartosc z boarda
            if board_value != 0:
                current_x = y
                current_y = x
                proper_x = (board_value - 1) % COL
                proper_y = (board_value - 1) // ROW  # floor division
                distance += abs(proper_x - current_x) + abs(proper_y - current_y)
    return distance  # trzeba dodac jeszcze glebokosc


def hamming_heuristic(board):
    distance = 0
    for number in range(0, COL * ROW):
        board_value = board[number]
        if number != board_value - 1 and board_value != 0:
            distance += 1
    return distance  # trzeba dodac jeszcze glebokosc


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
    visited.add(hash(tuple(board)))
    index = board.index(0)
    for move in priority:
        if move == "U" and int(index / COL) != 0:  # mozna sie ruszyc do góry   #index >= COL:
            if path == "" or path[-1] != "D":
                new_board = change_state(board, "U", index)
                if hash(tuple(new_board)) not in visited:
                    path += "U"  # path.append("U")
                    result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                    if result is not None:
                        return result
                    path = path[:-1]  # path.pop()
        elif move == "L" and index % COL != 0:  # ruch w lewo index % COL != 0
            if path == "" or path[-1] != "R":
                new_board = change_state(board, "L", index)
                if hash(tuple(new_board)) not in visited:
                    path += "L"
                    result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                    if result is not None:
                        return result
                    path = path[:-1]
        elif move == "D" and int(index / COL) != ROW - 1:  # ruch w dol  index < COL * ROW - COL
            if path == "" or path[-1] != "U":
                new_board = change_state(board, "D", index)
                if hash(tuple(new_board)) not in visited:
                    path += "D"
                    result = dfs_algorithm_v2(new_board, path, visited, current_depth + 1, priority)
                    if result is not None:
                        return result
                    path = path[:-1]
        elif move == "R" and index % COL != COL - 1:  # ruch w prawo  and (index + 1) % COL != 0 and index < COL * ROW - 1
            if path == "" or path[-1] != "L":
                new_board = change_state(board, "R", index)
                if hash(tuple(new_board)) not in visited:
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


print(f"odleglosc manhattan: {manhattan_heuristic(list_puzzle)}")
print(f"odleglosc hamminga: {hamming_heuristic(list_puzzle)}")
algorithm_result = None
if sys.argv[1] == "dfs":
    star_time = time.time_ns()
    algorithm_result = dfs_algorithm_v2(list_puzzle, "", set(), 0, priority)
    elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
    print(round(elapsed_time, 3))
    print(algorithm_result)
elif sys.argv[1] == "bfs":
    star_time = time.time_ns()
    algorithm_result = bfs_algorithm(list_puzzle, priority)
    elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
    print(round(elapsed_time, 3))
    print(algorithm_result)

with open(f"{sys.argv[4]}", "w") as file:  # otwiera plik i automatycznie go zamyka jak skoncze pisac
    if algorithm_result is not None:
        file.write(f"{len(algorithm_result)}\n{algorithm_result}")
    else:
        file.write("-1")

# TODO zamiast patrzec ostatni char ze stringa czy byl ruch to mzoesz przekazywac jako parametr
# TODO zawsze mozna zrobic liste i dodawac sasiadow
# TODO zrobic jakeis hashowanie do porównywania stanów w visited

# Step-by-step explanation:
#
# 1. We start by initializing the open and closed lists. The open list contains only the start node, and the closed list is initially empty.
#
# 2.We also initialize two dictionaries: cost, which contains the cost to reach each node from the start node, and parent,
# which contains the parent node of each node. For the start node, the cost is 0 and the parent is None.
#
# 3.We enter a loop that continues until the open list is empty.
#
# 4.In each iteration of the loop, we get the node with the lowest cost from the open list. We use a function h to estimate
# the remaining cost from the current node to the goal node. We add the estimated cost to the cost to reach the current node to get the total cost. This is used to select the node with the lowest total cost.
#
# 5. If the current node is the goal node, we have found a path from the start node to the goal node. We construct the path by
# following the parent pointers from the goal node to the start node, and then reverse the path to get the correct order. We return the path.
#
# 6. If the current node is not the goal node, we move it from the open list to the closed list.
#
# 7.We loop through the neighbors of the current node.
#
# 8.If a neighbor has already been evaluated (i.e., it is in the closed list), we skip it and move on to the next neighbor.
#
# 9.We calculate the tentative cost to reach the neighbor node by adding the cost to reach the current node to the cost
# to move from the current node to the neighbor node.
#
# 10.If the neighbor is not in the open list, or if the tentative cost is lower than the current cost to reach the
# neighbor, we update the cost and parent dictionaries for the neighbor node.
#
# 11.If the neighbor node is not already in the open list, we add it to the open list.
#
# 12.After all neighbors of the current node have been processed, we repeat the loop until the open list is empty.
#
# 13.If the loop completes without finding a path to the goal node, we return None to indicate that no path was found.
#
# Overall, the A* algorithm works by using heuristics to guide the search for the shortest path from the start node to
# the goal node. It uses a combination of the cost to reach each node and an estimate of the remaining cost to the goal
# node to determine which nodes to explore next. By exploring nodes with lower total cost first, it is able to find an
# optimal path from the start node to the goal node.


# def a_star(start, goal, heuristic_func):  pseudo code for A*
#     """
#     A* algorithm implementation.
#
#     :param start: The starting node.
#     :param goal: The goal node.
#     :param heuristic_func: A function that calculates the heuristic cost between two nodes.
#     :return: The path from start to goal.
#     """
#     # Initialize open and closed lists
#     open_list = [start]
#     closed_list = []
#
#     # Initialize the cost and the parent dictionary
#     cost = {start: 0}
#     parent = {start: None}
#
#     # Loop until the open list is empty
#     while open_list:
#         # Get the node with the lowest cost
#         current = min(open_list, key=lambda node: cost[node] + heuristic_func(node, goal))
#
#         # Check if the goal is reached
#         if current == goal:
#             path = []
#             while current is not None:
#                 path.append(current)
#                 current = parent[current]
#             path.reverse()
#             return path
#
#         # Move the current node from the open list to the closed list
#         open_list.remove(current)
#         closed_list.append(current)
#
#         # Loop through the neighbors of the current node
#         for neighbor in current.neighbors:
#             # Check if the neighbor is already evaluated
#             if neighbor in closed_list:
#                 continue
#
#             # Calculate the tentative cost to reach the neighbor node
#             tentative_cost = cost[current] + current.cost_to(neighbor)
#
#             # Check if the neighbor node is not in the open list
#             if neighbor not in open_list:
#                 open_list.append(neighbor)
#             # Check if the tentative cost is greater than or equal to the cost to reach the neighbor node
#             elif tentative_cost >= cost[neighbor]:
#                 continue
#
#             # Update the cost and parent dictionary
#             cost[neighbor] = tentative_cost
#             parent[neighbor] = current
#
#     # No path found
#     return None
