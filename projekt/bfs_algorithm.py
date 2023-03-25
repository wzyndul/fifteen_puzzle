from collections import deque


class Bfs:
    def __init__(self, board):
        self.board = board
        self.visited = set()
        self.visited_states = 1
        self.proceesed_states = 0

    def bfs_solve(self):
        q = deque([(self.board, "")])
        self.visited.add(self.board.__hash__())
        while q:
            state, path = q.popleft()
            self.proceesed_states += 1
            if state.is_solved():
                #self.proceesed_states += 1
                return path
            state.move()
            for neighbour in state.get_neighbors():
                self.visited_states += 1
                if neighbour.__hash__() not in self.visited:
                    self.visited.add(neighbour.__hash__())
                    q.append((neighbour, path + neighbour.last_move))
                    #self.visited_states += 1 ogolnie to zalezy od tego jakie zalozenie przyjmujemy co do odwiedzania stanow
                    #1. czy jesli wylosuje sie uklad jaki byl juz w visited to i tak go odwiedzamy, ale juz nie przetwarzamy
                    #2. nieodwiedzamy i nieprzetwarzamy
                    #tldr to notatka bardziej dla mnie bo znowu mam pewna rozkmine i musze z toba skonsultowac xdd obgadamy na spokojnie
                    #ale jak cos to na oba sposoby wiem jak to zrobic tylko idk ktory lepszy
        return None

    def states_counter(self):
        return self.visited_states , self.proceesed_states
