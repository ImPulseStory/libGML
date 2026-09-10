import pygame

class Mouse:
    def __init__(self):
        self.current = pygame.mouse.get_pressed()
        self.previous = self.current

    def mouseRightButtonDown(self):
        return self.current[2]

    def mouseRightButtonUp(self):
        return not self.current[2]

    def mouseRightButtonReleased(self):
        return not self.current[2] and self.previous[2]

    def mouseRightButtonClicked(self, rect):
        return self.mouseRightButtonReleased() and self.is_hover(rect)

    def mouseMiddleButtonDown(self):
        return self.current[1]

    def mouseMiddleButtonUp(self):
        return not self.current[1]

    def mouseMiddleButtonReleased(self):
        return not self.current[1] and self.previous[1]

    def mouseMiddleButtonClicked(self, rect):
        return self.mouseMiddleButtonReleased() and self.is_hover(rect)

    def mouseLeftButtonDown(self):
        return self.current[0]

    def mouseLeftButtonUp(self):
        return not self.current[0]

    def mouseLeftButtonReleased(self):
        return not self.current[0] and self.previous[0]

    def mouseLeftButtonClicked(self, rect):
        return self.mouseLeftButtonReleased() and self.is_hover(rect)

    def get_pressed(self):
        return pygame.mouse.get_pressed()

    def getPos(self):
        return pygame.mouse.get_pos()

    def is_hover(self, rect):
        return rect.collidepoint(self.getPos())

    def update(self):
        self.previous = self.current
        self.current = pygame.mouse.get_pressed()