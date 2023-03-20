import copy


class Board:
    def __init__(self, col, row, puzzle, priority):
        self.col = col
        self.row = row
        self.board = puzzle
        self.parent = None
        self.last_move = ''
        if priority == "hamm" or priority == "manh":  # jesli mam do czynienia z a starem
            self.priority = "LURD"  # to na sztywno daje wybrana kolejnosc
            self.heuristic = priority
        else:
            self.priority = priority
            self.heuristic = None
        self.neighbors = []
        self.depth = 1

    def get_neighbors(self):
        return self.neighbors

    def __copy__(self):
        new_board = copy.deepcopy(self.board)
        new_instance = Board(self.col, self.row, new_board, self.priority)
        new_instance.last_move = self.last_move
        new_instance.parent = self
        new_instance.priority = self.priority
        new_instance.depth = self.depth + 1
        new_instance.heuristic = self.heuristic
        return new_instance

    def __hash__(self):
        board_copy = self.board.copy()
        board_copy.append(self.depth)
        return hash(tuple(board_copy))

    def is_solved(self):  # sprawdzenie czy mamy rozwiązanie
        solution = list(range(1, self.row * self.col)) + [0]
        return tuple(self.board) == tuple(solution)

    def change_state(self, move, index):
        new_board = self.__copy__()
        new_board.last_move = move
        if move == "U":
            temp = new_board.board[index - self.col]
            new_board.board[index - self.col] = 0
            new_board.board[index] = temp
            return new_board

        elif move == "D":
            temp = new_board.board[index + self.col]
            new_board.board[index + self.col] = 0
            new_board.board[index] = temp
            return new_board

        elif move == "R":
            temp = new_board.board[index + 1]
            new_board.board[index + 1] = 0
            new_board.board[index] = temp
            return new_board

        elif move == "L":
            temp = new_board.board[index - 1]
            new_board.board[index - 1] = 0
            new_board.board[index] = temp
            return new_board
        return None

    def move(self):
        index = self.board.index(0)
        for move in self.priority:
            if move == "U" and self.last_move != "D" and int(
                    index / self.col) != 0:
                self.neighbors.append(self.change_state(move, index))
            elif move == "L" and self.last_move != "R" and index % self.col != 0:
                self.neighbors.append(self.change_state(move, index))
            elif move == "D" and self.last_move != "U" and int(
                    index / self.col) != self.row - 1:
                self.neighbors.append(self.change_state(move, index))
            elif move == "R" and self.last_move != "L" and index % self.col != self.col - 1:
                self.neighbors.append(self.change_state(move, index))

    def manhattan_heuristic(self):
        distance = 0
        for x in range(0, self.row):
            for y in range(0, self.col):
                board_value = self.board[x * self.row + y]  # wartosc z boarda
                if board_value != 0:
                    current_x = y
                    current_y = x
                    proper_x = (board_value - 1) % self.col
                    proper_y = (board_value - 1) // self.row  # floor division
                    distance += abs(proper_x - current_x) + abs(proper_y - current_y)
        return distance

    def hamming_heuristic(self):
        distance = 0
        for number in range(0, self.col * self.row):
            board_value = self.board[number]
            if number != board_value - 1 and board_value != 0:
                distance += 1
        return distance

    def get_heuristic_cost(self):
        if self.heuristic == "hamm":
            return self.hamming_heuristic()
        else:
            return self.manhattan_heuristic()

    def __lt__(self, other):  # musiałem zdefiniować less than "<" operator, zeby móc jakoś porównywać obiektu
        return True  # typu Board. Zwracam, true bo jak mają taki sam koszt to juz obojetnie, ktory pierwszy

    def __str__(self):
        result = ""
        for i in range(0, self.row):
            for j in range(0, self.col):
                result += str(self.board[self.row * i + j]) + " "
            result += "\n"
        print(result)
