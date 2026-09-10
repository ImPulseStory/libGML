import pygame

class TextInput():
    def __init__(self, x, y, width, height, color, hint, font, font_size, on_enter):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hint = hint
        self.text = ""
        self.active = False
        self.on_enter = on_enter
        self.font = pygame.font.Font(font, font_size) if font_size else pygame.font.SysFont(None, 24)
        self.cursor_visible = True
        self.cursor_timer = 0

    def update(self, mouse, keyboard, events):
        if mouse.mouseLeftButtonClicked(self.rect):
            self.active = True
        elif mouse.mouseLeftButtonReleased() and not mouse.is_hover(self.rect):
            pass

        if self.active:
            for event in events:
                if  event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.on_enter:
                            self.on_enter(self.text)
                    elif event.unicode:
                        self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        display_text = self.text if self.text else self.hint
        color = (255, 255, 255) if self.text else (150, 150, 150)
        text_surface = self.font.render(display_text, True, color)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))