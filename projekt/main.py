import numpy as np
import sys

from astr import Astr
from bfs_algorithm import Bfs
from board import Board
from dfs_algorithm import Dfs

algorithm_type = sys.argv[1]
priority = sys.argv[2]
with open(f"{sys.argv[3]}", "r") as f:  # wczytanie ukladanki z pliku
    rows, cols = np.fromfile(f, dtype=int, count=2, sep=" ")
    data = np.fromfile(f, dtype=int, count=rows * cols, sep=" ").reshape((rows, cols))

list_puzzle = data.flatten().tolist()  # zamiana z numpy array na liste
puzzle = Board(cols, rows, list_puzzle, priority)

algorithm_result = None
visited_states = None
processed_states = None
algorithm_time = None
max_recursion = None
if sys.argv[1] == "dfs":
    dfs = Dfs()
    algorithm_result = dfs.dfs_solve(puzzle)
    algorithm_time = dfs.algorithm_time()
    visited_states, processed_states = dfs.states_counter()
    max_recursion = dfs.recursion_reached()

elif sys.argv[1] == "bfs":
    bfs = Bfs(puzzle)
    algorithm_result = bfs.bfs_solve()
    algorithm_time = bfs.algorithm_time()
    visited_states, processed_states = bfs.states_counter()
    max_recursion = bfs.recursion_reached()


elif sys.argv[1] == "astr":
    astr = Astr(puzzle)
    algorithm_result = astr.astr_solve()
    algorithm_time = astr.algorithm_time()
    visited_states, processed_states = astr.states_counter()
    max_recursion = astr.recursion_reached()

with open(f"stats/{sys.argv[4]}", "w") as output_file:
    if algorithm_result is not None:
        output_file.write(f"{len(algorithm_result)}\n{algorithm_result}")
    else:
        output_file.write("-1")

with open(f"stats/{sys.argv[5]}", "w") as output_file:
    if algorithm_result is not None:
        output_file.write(f"{len(algorithm_result)}\n")
    else:
        output_file.write("-1\n")
    output_file.write(f"{visited_states}\n")
    output_file.write(f"{processed_states}\n")
    output_file.write(f"{max_recursion}\n")
    output_file.write(f"{algorithm_time}")
