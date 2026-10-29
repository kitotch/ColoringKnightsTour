import random
from collections import deque
class game:
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
        x, y = move
        self.board[x][y] = self.nextColor.popleft()
        nextColor.append(random.randrange(4))
        while True:
            clearPos = self.clearColor()
            for x1, y1 in clearPos:
                board[x1][y1] = -1
            if len(clearPos) == 0:
                break
    def clearColor(self):
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x in range(8):
            for y in range(8):
                c = self.board[x][y]
                if c != -1:
                    q = deque([(x, y)])
                    while len(q) > 0:
                        for dx, dy in d:
                            x1, y1 = x + dx, y + dy
                            if 0 <= x1 < 8 and 0 <= y1 < 8:
                                while self.board[x1][y1] == -1:
                                    x1 += dx
                                    y1 += dy
                                    if not (0 <= x1 < 8 and 0 <= y1 < 8):
                                        break
                                else:
                                    if self.board[x1][y1] == c:
