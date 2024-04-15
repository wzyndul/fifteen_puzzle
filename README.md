<h1 align="center" id="title">Fifteen Puzzle Solver</h1>

<p id="description">This is a consol application that search through graph using three different algorithms: BFS, DFS and A* to solve initial puzzle loaded from a file. It also provides statistical data of each algorithm run.</p>    

<h2> 🧩  Problem Explanation </h2>
Fifteen is a classic puzzle game played on a 4x4 board filled with numbered tiles from 1 to 15 and one empty space. Players can slide tiles vertically or horizontally into the empty space. The objective is to rearrange the tiles into ascending numerical order, with the empty space in the bottom right corner. Solving the game involves exploring a graph where the initial state of the board is the root, and subsequent vertices represent child states resulting from moving tiles according to the game rules. This exploration is done using three different strategies: Breadth-First Search (BFS), Depth-First Search (DFS), and A*.


In this project, these three algorithms are utilized to solve all puzzles from the puzzles directory. In the research part, the three algorithms run through all eight possible priority move orders. All results that display statistics on performance of algorithms are shown in the report.pdf (in polish).




<h2>💻 Built with</h2>

Technologies used in the project:
* Python with numpy library

<h2>🛠️ Installation Steps</h2>

To get started with this project, clone the repository and install the dependencies:

```
pip install -r "requirements.txt"
```
To run application type in console:
```
python main.py bfs RDUL 4x4_01_00001.txt 4x4_01_00001_bfs_rdul_sol.txt 4x4_01_00001_bfs_rdul_stats.txt
```
where:

first parameter is algorithm name (bfs, dfs, astr)

second is move priority order (R - right, D - down, L - left, U - up)

third is a file name with initial position to solve (all files are in puzzles directory)

fourth is a file name where application saves solution of the initial problem

fifth is a file name where applciation saves stats 


