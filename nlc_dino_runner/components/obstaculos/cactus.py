import random
from nlc_dino_runner.components.obstaculos.obstacle import Obstacle
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class Cactus(Obstacle):
    def __init__(self):
        self.list_index = random.randint(0, 2)
        png_array = [SMALL_CACTUS, LARGE_CACTUS, BIRD][self.list_index]
        if self.list_index == 2:
            super().__init__(png_array, True)
            self.rect.y = 285
        else:
            super().__init__(png_array)
            self.rect.y = 350 if self.list_index == 0 else 330