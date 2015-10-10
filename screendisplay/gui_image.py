import gui_item
import pygame

class gui_image(gui_item.gui_item):
    def __init__(self, image_path):
        gui_item.gui_item.__init__(self, "image")
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))