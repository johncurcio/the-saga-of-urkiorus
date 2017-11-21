import pygame
from constants import *

#Sets the width and height of the screen
#WIDTH = DISPLAY_WIDTH
#HEIGHT = DISPLAY_HEIGHT

#Initializes the screen - Careful: all pygame commands must come after the init
#pygame.init()

#Sets the screen note: must be after pygame.init()
#screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.image.fill((13,13,13))
        self.image.set_colorkey((13,13,13))
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("monospace", 18)

    def add(self, letter, pos):
        s = self.font.render(letter, 1, RGB_WHITE)
        self.image.blit(s, pos)

class Cursor(pygame.sprite.Sprite):
    def __init__(self, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(RGB_BLACK)
        self.text_height = 17
        self.text_width = 10
        self.rect = self.image.get_rect(topleft=(self.text_width, self.text_height))
        self.board = board
        self.text = ' '
        self.cooldown = 0
        self.cooldowns = {'.': 1,
                        '[': 1,
                        ']': 1,
                        ' ': 5,
                        '\n': 30}

    def write(self, text):
        self.text = list(text)

    def update(self):
        if not self.cooldown and self.text:
            letter = self.text.pop(0)
            if letter == '\n':
                self.rect.move_ip((0, self.text_height))
                self.rect.x = self.text_width
            else:
                self.board.add(letter, self.rect.topleft)
                self.rect.move_ip((self.text_width, 0))
            self.cooldown = self.cooldowns.get(letter, 8)

        if self.cooldown:
            self.cooldown -= 1

class Intro:
    def __init__(self, screen, text, quit=True, speed_multiplier=3, wait=2000):
        self.screen = screen
        self.text = text
        self.quit = quit
        self.speed_multiplier = speed_multiplier
        self.wait = wait

    def run(self):
        clock = pygame.time.Clock()
        all_sprites = pygame.sprite.Group()
        board = Board()
        cursor = Cursor(board)
        all_sprites.add(cursor, board)
        cursor.write(self.text)
        running = True
        while running:
            if len(cursor.text)==0:
                pygame.time.wait(self.wait)
                running = not self.quit
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
            
            all_sprites.update()
            self.screen.fill(RGB_BLACK)
            all_sprites.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS*self.speed_multiplier)


#text = """[i] Initializing ...
#[i] Entering ghost mode ...

#done ...

#"""

#intro = Intro(screen, text)
#intro.run()


#text = """another text

#sasdasd"""

#intro = Intro(screen, text, False)
#intro.run()