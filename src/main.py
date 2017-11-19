import pygame
from background import Background
from constants import *

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        pygame.display.update()
        clock.tick(FPS)

def text_objects(text, font):
    textSurface = font.render(text, True, RGB_WHITE)
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        BackGround = Background(BACKGROUND_INTRO, BACKGROUND_INTRO_POS)
        screen.blit(BackGround.image, BackGround.rect)
        largeText = pygame.font.SysFont(FONT_INTRO,FONT_INTRO_SIZE)
        TextSurf, TextRect = text_objects(GAME_TITLE, largeText)
        TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/3))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

game_intro()
game_loop()
pygame.quit()
quit()