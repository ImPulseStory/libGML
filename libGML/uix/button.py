import pygame

class Button:
    def __init__(self, x, y, width, height, color, text, on_click, font, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.on_click = on_click
        self.font = pygame.font.Font(font, font_size) if font_size else pygame.font.SysFont(None, 24)
        self.hover_color = (min(color[0] + 30, 255), min(color[1] + 30, 255), min(color[2] + 30, 255))
        self.is_hover = False

    def update(self, mouse, keyboard, events):
        self.is_hover = mouse.is_hover(self.rect)
        if mouse.mouseLeftButtonClicked(self.rect) and self.on_click:
            self.on_click()

    def draw(self, surface):
        color = self.hover_color if self.is_hover else self.color
        pygame.draw.rect(surface, color, self.rect)
        if self.text:
            text_surface = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)