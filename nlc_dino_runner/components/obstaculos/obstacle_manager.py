import pygame.time

from nlc_dino_runner.utils.constants import SMALL_CACTUS
from nlc_dino_runner.components.obstaculos.cactus import Cactus
from nlc_dino_runner.utils.constants import GAME_SPEED, DEFAULT_TYPE


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacle_position = None

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus())
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles, game)
            self.obstacle_position = obstacle.rect
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                else:
                    game.power_up_manager.reset_power_ups(game.points)
                    game.dino_lives.update_list()
                    self.reset_obstacles()
                    if game.dino_lives.trigger:
                        self.death_protocol(game)
                    break

            if game.hammer_tool_manager.hammer_collision:
                self.obstacles.remove(obstacle)

    def death_protocol(self, game):
        game.death_count_print = True
        game.playing = False
        game.game_speed = GAME_SPEED
        game.points = 0
        game.death_count += 1
        game.player.type = DEFAULT_TYPE
        game.dino_lives.reset_hearts_block()
        game.power_up_manager.reset_power_ups(game.points)
        self.reset_obstacles()
        game.hammer_tool_manager.reset()
        pygame.time.delay(100)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
