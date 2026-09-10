import pygame

class Label:
    def __init__(self, x, y, width, height, color, text, font, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(font, font_size) if font_size else pygame.font.SysFont(None, 24)

    def update(self, mouse, keyboard, events):
        pass

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def set_text(self, text):
        self.text = text

    def set_color(self, color):
        self.color = color