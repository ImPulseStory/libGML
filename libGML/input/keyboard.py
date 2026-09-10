import pygame

class Keyboard:
    def __init__(self):
        self.keyses = {
            "W": pygame.K_w,
            "A": pygame.K_a,
            "S": pygame.K_s,
            "D": pygame.K_d,
            "Q": pygame.K_q,
            "E": pygame.K_e,
            "R": pygame.K_r,
            "T": pygame.K_t,
            "U": pygame.K_u,
            "V": pygame.K_v,
            "UP": pygame.K_UP,
            "DOWN": pygame.K_DOWN,
            "LEFT": pygame.K_LEFT,
            "RIGHT": pygame.K_RIGHT,
            "Y": pygame.K_y,
            "Z": pygame.K_z,
            "I": pygame.K_i,
            "J": pygame.K_j,
            "K": pygame.K_k,
            "L": pygame.K_l,
            "M": pygame.K_m,
            "N": pygame.K_n,
            "O": pygame.K_o,
            "P": pygame.K_p,
            "SPACE": pygame.K_SPACE,
            "BACKSPACE": pygame.K_BACKSPACE,
            "RETURN": pygame.K_RETURN,
            "SLASH": pygame.K_SLASH,
            "1": pygame.K_1,
            "2": pygame.K_2,
            "3": pygame.K_3,
            "4": pygame.K_4,
            "5": pygame.K_5,
            "6": pygame.K_6,
            "7": pygame.K_7,
            "8": pygame.K_8,
            "9": pygame.K_9,
            "0": pygame.K_0,
            "ESCAPE": pygame.K_ESCAPE,
            "PLUS": pygame.K_PLUS,
            "MINUS": pygame.K_MINUS,
            "CAPSLOCK": pygame.K_CAPSLOCK,
            "TAB": pygame.K_TAB,
            "LSHIFT": pygame.K_LSHIFT,
            "RSHIFT": pygame.K_RSHIFT,
            "ALT": pygame.KMOD_ALT,
            "LCONTROL": pygame.K_LCTRL,
            "RCONTROL": pygame.K_RCTRL,
            "F1": pygame.K_F1,
            "F2": pygame.K_F2,
            "F3": pygame.K_F3,
            "F4": pygame.K_F4,
            "F5": pygame.K_F5,
            "F6": pygame.K_F6,
            "F7": pygame.K_F7,
            "F8": pygame.K_F8,
            "F9": pygame.K_F9,
            "F10": pygame.K_F10,
            "F11": pygame.K_F11,
            "F12": pygame.K_F12,
            "F13": pygame.K_F13,
            "F14": pygame.K_F14,
            "F15": pygame.K_F15,
        }
        self.keys = pygame.key.get_pressed()
        self.text_input = ""
        self.backspace = False
    
    def is_pressed(self, key) -> bool:
        self.keys = pygame.key.get_pressed()
        if not self.keys[self.keyses.get(key)]:
            return False
        return self.keys[self.keyses[key]]

    def update(self, events):
        self.keys = pygame.key.get_pressed()
        self.backspace = False
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.backspace = True
                elif event.key == pygame.K_RETURN:
                    self.enter_pressed = True
                else:
                    if event.unicode:
                        self.text_input += event.unicode

    def get_pressed(self):
        return self.keys

    def get_text_input(self):
        return self.text_input

    def clear_text_input(self):
        self.text_input = ""