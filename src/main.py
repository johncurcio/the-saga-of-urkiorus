import pygame
from background import Background
from option import Option
from intro import Intro
from fader import Fader
from constants import *

BackGround = Background(BACKGROUND_INTRO, BACKGROUND_INTRO_POS)
sound1 = Fader(MAIN_MENU_SONG)
sound2 = Fader(INTRO_SONG)

def game_intro():
    screen.fill(RGB_BLACK) #DRAWS MENU
    pygame.display.update()
    sound1.sound.set_volume(0)
    pygame.time.wait(100)
    sound2.sound.play()
    text = """[i] Initializing ...
[i] Entering ghost mode ...

done ..."""
    Intro(screen, text).run()
    Intro(screen, "End.", False).run()


def game_loop():
    game_exit = False
    game_intro() 
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
               
        pygame.display.update()
        clock.tick(FPS)

def text_objects(text, font):
    textSurface = font.render(text, True, RGB_WHITE)
    return textSurface, textSurface.get_rect()

def draw_menu(options):
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
            option.execute()
        else:
            option.hovered = False
        option.draw()

def game_menu(options):
    intro = True
    sound1.sound.play()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(BackGround.image, BackGround.rect)
        largeText = pygame.font.Font(FONT_INTRO,FONT_INTRO_SIZE)
        TextSurf, TextRect = text_objects(GAME_TITLE, largeText)
        TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/3))
        screen.blit(TextSurf, TextRect)
        draw_menu(options)
        pygame.display.update()
        clock.tick(FPS)

def quit_game():
    pygame.quit()
    quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()
    menu_font = pygame.font.Font(FONT_INTRO, 50)
    options = [Option("new game",  (320, 300), menu_font, screen, game_loop), 
               Option("load game", (320, 350), menu_font, screen),
               Option("quit",      (320, 400), menu_font, screen, quit_game)]
    game_menu(options)
