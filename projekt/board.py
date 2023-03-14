class Board:
    def __init__(self, puzzle, row, col):
        self.puzzle = puzzle
        self.row = row
        self.col = col

    def change_state(self, move, index):
        new_puzzle = self.puzzle.copy()
        if move == "U":
            temp = new_puzzle[index - self.col]
            new_puzzle[index - self.col] = 0
            new_puzzle[index] = temp
            return new_puzzle

        elif move == "D":
            temp = new_puzzle[index + self.col]
            new_puzzle[index + self.col] = 0
            new_puzzle[index] = temp
            return new_puzzle

        elif move == "R":
            temp = new_puzzle[index + 1]
            new_puzzle[index + 1] = 0
            new_puzzle[index] = temp
            return new_puzzle

        elif move == "L":
            temp = new_puzzle[index - 1]
            new_puzzle[index - 1] = 0
            new_puzzle[index] = temp
            return new_puzzle
        return None

    def is_solved_v2(self):
        solution = list(range(1, self.row * self.col)) + [0]
        return self.puzzle == tuple(solution)
