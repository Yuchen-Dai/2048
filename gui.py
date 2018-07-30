import G2048, pygame, random


class Gui:

    def __init__(self):
        self._running = True
        self.activate_ai = True
        self.fps = 60
        self.board = G2048.Board(4,4)
        self.board.create_random_block()

    def run(self):
        pygame.init()
        self._resize_surface((600,600))
        clock = pygame.time.Clock()
        count = 1
        while self._running:
            clock.tick(self.fps)
            try:
                self._handle_events()
                if count == 10:
                    count = 1
                    self.ai()
                self._redraw()
                count += 1
            except ValueError:
                pass
        pygame.quit()

    def ai(self):
        if self.activate_ai:
            pick = random.randint(273,276)
            self._handle_keydown(pick)
    
    def _redraw(self):
        surface = pygame.display.get_surface()

        surface.fill((255,255,255))

        self._draw_board()

        pygame.display.flip()

    def _draw_board(self):
        surface = pygame.display.get_surface()
        width = surface.get_width()
        height = surface.get_height()

        font = pygame.font.Font(None, 50)
        r = 0
        for row in self.board.get_board():
            c = 0
            for col in row:
                place = (100 + c * 100, 100 + r * 100, 100, 100)
                if not ((r + c) % 2):
                    pygame.draw.rect(surface, (219,103,112), place)
                else:
                    pygame.draw.rect(surface, (174,221,223), place)
                if not col:
                    col = ' '
                num = font.render(f'{col: <5}', True, (0, 0, 0))
                surface.blit(num, place)
                c += 1
            r += 1
                

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            elif not self.activate_ai and event.type == pygame.KEYDOWN:
                self._handle_keydown(event.key)


    def _handle_keydown(self,key):
        if key < 277 and key > 272:
            self.board.check_gameover()

        if key == 276:
            if self.board.left():
                self.board.create_random_block()
        elif key == 273:
            if self.board.up():
                self.board.create_random_block()
        elif key == 275:
            if self.board.right():
                self.board.create_random_block()
        elif key == 274:
            if self.board.down():
                self.board.create_random_block()
        elif key == 27:
            self._end_game()
        elif key == 114:
            self.board = G2048.Board(4, 4)
            self.board.create_random_block()

    def _end_game(self):
        self._running = False
        
    def _resize_surface(self, size):
        pygame.display.set_mode(size)

if __name__ == '__main__':
    Gui().run()
