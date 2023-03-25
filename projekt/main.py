import numpy as np
import sys
import time

from astr import Astr
from bfs_algorithm import Bfs
from board import Board
from dfs_algorithm import Dfs

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

algorithm_result = None
if sys.argv[1] == "dfs":
    dfs = Dfs()
    star_time = time.time_ns()
    algorithm_result = dfs.dfs_solve(puzzle)
    elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
    print(round(elapsed_time, 3))
    print(algorithm_result)
    visited_states, proceseed_states = dfs.states_counter()
    print(visited_states)
    print(proceseed_states)
elif sys.argv[1] == "bfs":
    bfs = Bfs(puzzle)
    star_time = time.time_ns()
    algorithm_result = bfs.bfs_solve()
    elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
    print(round(elapsed_time, 3))
    print(algorithm_result)
    visited_states, proceseed_states = bfs.states_counter()
    print(visited_states)
    print(proceseed_states)

elif sys.argv[1] == "astr":
    astr = Astr(puzzle)
    star_time = time.time_ns()
    algorithm_result = astr.astr_solve()
    elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
    print(round(elapsed_time, 3))
    print(algorithm_result)

with open(f"{sys.argv[4]}", "w") as file:  # otwiera plik i automatycznie go zamyka jak skoncze pisac
    if algorithm_result is not None:
        file.write(f"{len(algorithm_result)}\n{algorithm_result}")
    else:
        file.write("-1")
