import random
import pygame
from nlc_dino_runner.components.powerups.shell import Shield
from nlc_dino_runner.components.powerups.hammer import Hammer
from nlc_dino_runner.components.powerups.hammer_tool import Hammer_Tool
from nlc_dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 500)
        self.points = 0
        self.dino_status = False

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self):
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                if random.randint(0, 20) <= 10:
                    self.power_ups.append(Shield())
                else:
                    self.power_ups.append(Hammer())

    def update(self, points, game_speed, game):
        self.points = points
        self.generate_power_ups()

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                print('Dino has the', power_up.type)
                if power_up.type == HAMMER_TYPE:
                    game.player.type = power_up.type
                    game.hammer_tool_manager.dino_status = True
                    game.player.hammer = True
                    game.hammer_tool_manager.hammer_tools = [Hammer_Tool()] * 3
                    self.power_ups.remove(power_up)

                else:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.shield = True
                    game.player.show_text = True
                    game.player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    game.player.shield_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)