import pygame
from ..utils.constants import (
    TITLE,
    ICON,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BG,
    FPS
)

#class 2: game init and draw background

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_position_initial = 0
        self.y_position_initial = 400
        self.game_speed = 20
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_bakcground()
        pygame.display.flip()

    def draw_bakcground(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_position_initial, self.y_position_initial))
        self.screen.blit(BG, (image_width + self.x_position_initial, self.y_position_initial))

        if self.x_position_initial <= -image_width:
            self.screen.blit(BG, (image_width + self.x_position_initial, self.y_position_initial))
            self.x_position_initial = 0

        self.x_position_initial -= self.game_speed