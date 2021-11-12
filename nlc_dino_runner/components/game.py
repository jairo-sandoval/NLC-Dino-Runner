import pygame
from nlc_dino_runner.utils.text_utils import get_score_element, get_centered_message
from nlc_dino_runner.components.dinosaurio import Dinosaurio
from nlc_dino_runner.components.obstaculos.obstacle_manager import ObstacleManager
from nlc_dino_runner.utils.constants import (
    TITLE,
    ICON,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BG,
    FPS
)


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
        self.player = Dinosaurio()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.death_count = 0

    def run(self):
        self.points = 0
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_position_initial, self.y_position_initial))
        self.screen.blit(BG, (image_width + self.x_position_initial, self.y_position_initial))
        if self.x_position_initial <= -image_width:
            self.screen.blit(BG, (image_width + self.x_position_initial, self.y_position_initial))
            self.x_position_initial = 0

        self.x_position_initial -= self.game_speed

    def show_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

    def print_menu_elements(self):
        half_width = SCREEN_WIDTH // 2
        half_height = SCREEN_HEIGHT // 2
        text_element, text_element_rec = get_centered_message('Press any key to start')
        self.screen.blit(text_element, text_element_rec)
        text_element, text_element_rec = get_centered_message('Death Count: ' + str(self.death_count), height= half_height + 50)
        self.screen.blit(text_element, text_element_rec)
        self.screen.blit(ICON, (half_width - 40 , half_height - 150))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def score(self):
        self.points += 1
        if self.points % 20 == 0:
            self.game_speed += 1
        score_element, score_element_rect = get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)

