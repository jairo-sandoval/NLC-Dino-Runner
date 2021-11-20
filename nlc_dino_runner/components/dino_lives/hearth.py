from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART, HEARTS_NUMBER

class Heart(Sprite):
    def __init__(self):
        self.image = HEART
        self.image_width = HEART.get_width()
        self.hearts_number = HEARTS_NUMBER
        self.trigger = False
        self.image_y_pos = 20
        coord_list = [(x * self.image_width, self.image_y_pos) for x in range(1, self.hearts_number + 1)]
        self.images_list = [(HEART, coord) for coord in coord_list]
        self.temporary_list = self.images_list.copy()

    def draw(self, screen):
        self.trigger = False if not self.hearts_number <= 1 else True
        screen.blits(self.temporary_list)

    def update_list(self):
        self.temporary_list.pop()
        self.hearts_number -= 1

    def reset_hearts_block(self):
        self.hearts_number = HEARTS_NUMBER
        self.temporary_list = self.images_list.copy()