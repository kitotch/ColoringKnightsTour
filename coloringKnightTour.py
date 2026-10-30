import random
from collections import deque

# 自作ゲーム Coloring Knight's Tour
class Game:
    def __init__(self):
        self.nextColor = deque([random.randrange(4) for _ in range(3)])
        self.pos = (random.randrange(8), random.randrange(8))
        self.board = [[-1] * 8 for _ in range(8)]
        self.board[self.pos[0]][self.pos[1]] = random.randrange(4)
        self.score = 0
    def gen_moves(self):
        x, y = self.pos
        d = [(1, 2), (2, 1), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1)]
        movesLst = []
        for dx, dy in d:
            x1, y1 = x + dx, y + dy
            if 0 <= x1 < 8 and 0 <= y1 < 8 and self.board[x1][y1] == -1:
                movesLst.append((x1, y1))
        return movesLst
    def make_a_move(self, move):
        self.pos = move
        self.board[self.pos[0]][self.pos[1]] = self.nextColor.popleft()
        self.nextColor.append(random.randrange(4))
        chain = 0
        while True:
            clearPos = self.getClearPos()
            for x1, y1 in clearPos:
                self.board[x1][y1] = -1
            if len(clearPos) == 0:
                break
            self.score += len(clearPos) * 2 ** chain
            chain += 1
    def getClearPos(self):
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * 8 for _ in range(8)]
        clearPos = []
        for x in range(8):
            for y in range(8):
                c = self.board[x][y]
                if c != -1 and not visited[x][y]:
                    q = deque([(x, y)])
                    visited[x][y] = True
                    pos = []
                    while len(q) > 0:
                        nowX, nowY = q.popleft()
                        pos.append((nowX, nowY))
                        for dx, dy in d:
                            x1, y1 = nowX + dx, nowY + dy
                            if 0 <= x1 < 8 and 0 <= y1 < 8:
                                while self.board[x1][y1] == -1:
                                    x1 += dx
                                    y1 += dy
                                    if not (0 <= x1 < 8 and 0 <= y1 < 8):
                                        break
                                else:
                                    if self.board[x1][y1] == c and not visited[x1][y1]:
                                        q.append((x1, y1))
                                        visited[x1][y1] = True
                    if len(pos) >= 4:
                        clearPos.extend(pos)
        return clearPos
    def play(self):
        alphabet = "ABCD"
        while True:
            moves = self.gen_moves()
            if len(moves) == 0:
                print("Game Over")
                print(f"Score: {self.score}")
                return
            print("score:", self.score)
            print("      0     1     2     3     4     5     6     7")
            for i in range(8):
                print(f"{i} ", end="")
                for j in range(8):
                    print("[", end="")
                    if self.pos == (i, j):
                        print("N", end=" ")
                    else:
                        print(" ", end=" ")
                    if self.board[i][j] == -1:
                        print("_", end="")
                    else:
                        print(alphabet[self.board[i][j]], end="")
                    print("]", end=" ")
                print()
            flag = True
            while flag:
                print("Please input next move")
                try:
                    move = input()
                    x, y = map(int, move.split())
                    if (x, y) in moves:
                        flag = False
                    else:
                        print("Your input is illegal")
                except ValueError:
                    print("Your input is illegal")
            self.make_a_move((x, y))
    def new_game(self):
        self.__init__()

game1 = Game()
game1.play()
