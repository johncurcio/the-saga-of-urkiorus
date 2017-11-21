import pygame

class Option:
    hovered = False
    def __init__(self, text, pos, font, screen, action=None):
        self.text = text
        self.pos = pos
        self.menu_font = font
        self.screen = screen
        self.action = action
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        self.screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = self.menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def execute(self):
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and self.action != None:
            self.action()