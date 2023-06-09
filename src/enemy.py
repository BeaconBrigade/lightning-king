import pygame
from entity import Entity
from asset_manager import AssetManager


class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.position = [64, 63]
        self.vector = [0, 0]
        self.max_speed = 20
        self.current_speed = [0, 0]
        self.acceleration = 5
        self.texture = AssetManager.load_texture("enemy.png")

    def draw(self, view: pygame.surface.Surface, relative_pos: (int, int)):
        view.blit(self.texture, self.position)

    def update(self, entity_list: list[Entity]):
        # speed up or slow down depending on vector
        if self.vector[0] != 0:
            self.current_speed[0] = min(
                self.current_speed[0] + self.acceleration, self.max_speed
            )
        else:
            self.current_speed[0] = max(self.current_speed[0] - self.acceleration, 0)
        if self.vector[1] != 0:
            self.current_speed[1] = min(
                self.current_speed[1] + self.acceleration, self.max_speed
            )
        else:
            self.current_speed[1] = max(self.current_speed[1] - self.acceleration, 0)

        # update new position
        new_x = self.position[0] + self.vector[0] * self.current_speed[0]
        new_y = self.position[1] + self.vector[1] * self.current_speed[1]
        self.position = [new_x, new_y]
