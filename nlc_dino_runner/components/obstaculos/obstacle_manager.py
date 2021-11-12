import pygame.time

from nlc_dino_runner.utils.constants import SMALL_CACTUS
from nlc_dino_runner.components.obstaculos.cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            collide = pygame.Rect.colliderect(game.player.dino_rect, obstacle.rect)

            if game.player.dino_rect.colliderect(obstacle.rect):
                game.death_count += 1
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
