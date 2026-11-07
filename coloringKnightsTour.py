import pygame, random
from collections import deque

class Game:
    def __init__(self):
        self.nextColor = [random.randrange(4) for _ in range(3)]
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
        self.board[self.pos[0]][self.pos[1]] = self.nextColor.pop(0)
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
        color = {
            -1: (0xDF, 0xDF, 0xDF),
            0: (0xDF, 0x40, 0x40),
            1: (0x40, 0xDF, 0x40),
            2: (0x40, 0x40, 0xDF),
            3: (0xDF, 0xDF, 0x40)
        }

        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Coloring Knight's Tour")
        clock = pygame.time.Clock()

        try:
            font = pygame.font.SysFont("segoeuisymbol", 20)
        except:
            font = pygame.font.Font(None, 20)

        knight = font.render("\u265E", True, (0, 0, 0))
        
        text_next = font.render("NEXT", True, (0, 0, 0))

        text_game_over = font.render("GAME OVER", True, (0, 0, 0))
        text_new_game = font.render("new game", True, (0, 0, 0))

        running = True
        moves = self.gen_moves()
        while running:
            screen.fill((0xFF, 0xFF, 0xFF))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    if 40 <= click_x < 320 and 40 <= click_y < 320 and (click_x - 40) % 35 < 30 and (click_y - 40) % 35 < 30:
                        x, y = (click_x - 40) // 35, (click_y - 40) // 35
                        if (x, y) in moves:
                            self.make_a_move((x, y))
                            moves = self.gen_moves()
                    if len(moves) == 0 and 335 <= click_x < 435 and 285 <= click_y < 320:
                        self.new_game()
                        moves = self.gen_moves()

            pygame.draw.rect(screen, 0xBFBFBF, (30, 30, 295, 295))
            for i in range(8):
                for j in range(8):
                    x, y = 40 + i * 35, 40 + j * 35
                    pygame.draw.rect(screen, color[self.board[i][j]], (x, y, 30, 30))

            x, y = 45 + self.pos[0] * 35, 40 + self.pos[1] * 35
            screen.blit(knight, (x, y))

            pygame.draw.rect(screen, 0xBFBFBF, (335, 35, 40, 110))

            for i in range(3):
                pygame.draw.rect(screen, color[self.nextColor[i]], (340, 40 + i * 35, 30, 30))

            screen.blit(text_next, (332, 15))

            text_score = font.render(f"SCORE: {self.score}", True, (0, 0, 0))
            screen.blit(text_score, (335, 150))

            if len(moves) == 0:
                pygame.draw.rect(screen, 0xBFBFBF, (335, 285, 100, 35))
                screen.blit(text_game_over, (335, 250))
                screen.blit(text_new_game, (340, 285))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
    def new_game(self):
        self.__init__()

if __name__ == "__main__":
    game1 = Game()
    game1.play()
