import copy


class Board:
    def __init__(self, col, row, puzzle):
        self.col = col
        self.row = row
        self.board = puzzle
        self.parent = None
        self.last_move = ''

    def __copy__(self):
        new_board = copy.deepcopy(self.board)
        new_instance = Board(self.col, self.row, new_board)
        new_instance.last_move = self.last_move
        new_instance.parent = self.parent
        return new_instance

    def __hash__(self):
        return hash(tuple(self.board))

    def is_solved(self):
        solution = list(range(1, self.row * self.col)) + [0]
        return tuple(self.board) == tuple(solution)

    def change_state(self, board, move, index):
        new_board = board.copy()
        if move == "U":
            temp = new_board[index - self.col]
            new_board[index - self.col] = 0
            new_board[index] = temp
            return new_board

        elif move == "D":
            temp = new_board[index + self.col]
            new_board[index + self.col] = 0
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

    def move(self, priority):
        index = self.board.index(0)
        for move in priority:
            if move == "U" and int(index / self.col) != 0:  # mozna sie ruszyc do góry   #index >= COL:
                pass
            elif move == "L" and index % self.col != 0:  # ruch w lewo index % COL != 0
                pass
            elif move == "D" and int(index / self.col) != self.row - 1:  # ruch w dol  index < COL * ROW - COL
                pass
            elif move == "R" and index % self.col != self.col - 1:  # ruch w prawo  and (index + 1) % COL != 0 and index < COL * ROW - 1

