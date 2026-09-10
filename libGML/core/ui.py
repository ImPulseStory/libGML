import pygame

from ..uix.label import Label
from ..uix.button import Button
from ..uix.panel import Panel
from ..uix.textinput import TextInput

class UI:
    def __init__(self):
        self.elements = []

    def create_button(self, x, y, width, height, color, text='', on_click=None, font=None, font_size=None):
        button = Button(x, y, width, height, color, text, on_click, font, font_size)
        self.elements.append(button)
        return button

    def create_label(self, x, y, width, height, color, text='', font=None, font_size=None):
        label = Label(x, y, width, height, color, text, font, font_size)
        self.elements.append(label)
        return label

    def create_panel(self, x, y, width, height, color):
        panel = Panel(x, y, width, height, color)
        self.elements.append(panel)
        return panel

    def create_textInput(self, x, y, width, height, color, hint='', font=None, font_size=None, on_enter=None):
        textInput = TextInput(x, y, width, height, color, hint, font, font_size, on_enter)
        self.elements.append(textInput)
        return textInput

    def update(self, mouse, keyboard, events):
        for element in self.elements:
            element.update(mouse, keyboard, events)

    def draw(self, screen):
        for element in self.elements:
            element.draw(screen)