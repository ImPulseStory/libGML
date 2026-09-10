import pygame
import json
import csv

from libGML.input.keyboard import Keyboard


class World:
    def __init__(self, sc):
        self.sc = sc
        self.interactables = {}
        self.keyboard = Keyboard()

    def load_room_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def draw_tile(self, atlas_name, x, y, atlas):
        wall = atlas.get(atlas_name)
        self.sc.blit(wall, (x, y))

    def load_room_csv(self, filename):
        with open(filename) as f:
            reader = csv.reader(f)
            return list(reader)

    def trigger_tile(self, player_rect, tile_size, map, tile):
        if map is None:
            return None

        col = player_rect.centerx // tile_size
        row = player_rect.centery // tile_size

        rows = len(map)
        if rows == 0:
            return False
        cols = len(map[0])

        if not (0 <= row < rows and 0 <= col < cols):
            return False

        tile_id = map[row][col]
        key = str(tile_id) if isinstance(tile_id, int) else tile_id
        return key == tile

    def draw_layer(self, map, atlas, width, height, camera):
        rows = len(map)
        cols = len(map[0]) if rows > 0 else 0

        start_x = max(0, int(camera.x // width))
        start_y = max(0, int(camera.y // height))
        end_x = min(cols, int((camera.x + self.sc.get_width()) // width) + 1)
        end_y = min(rows, int((camera.y + self.sc.get_height()) // height) + 1)

        self.map = map
        for row in range(start_y, end_y):
            for col in range(start_x, end_x):
                tile_id = map[row][col]
                if tile_id in atlas:
                    sc_x = (col * width) - camera.x
                    sc_y = (row * height) - camera.y
                    self.draw_tile(tile_id, sc_x, sc_y, atlas)

    def can_move_to(self, rect, tile_size, blocked_tiles, map):
        corners = [
            (rect.left, rect.top),
            (rect.right - 1, rect.top),
            (rect.left, rect.bottom - 1),
            (rect.right - 1, rect.bottom - 1)
        ]
        for cx, cy in corners:
            mx = int(cx // tile_size)
            my = int(cy // tile_size)
            if not (0 <= my < len(map) and 0 <= mx < len(map[0])):
                return False
            if map[my][mx] in blocked_tiles:
                return False
        return True

    def add_interactable(self, tile_id, trigger="E"):
        self.interactables[str(tile_id)] = {
            "trigger": trigger
        }

    def check_interactables(self, player_rect, map, tile_size):
        col = player_rect.centerx // tile_size
        row = player_rect.centery // tile_size

        if not (0 <= row < len(map) and 0 <= col < len(map[0])):
            return

        tile_id = str(map[row][col])
        if tile_id in self.interactables:
            if self.keyboard.is_pressed(self.interactables[tile_id]['trigger']):
                return True

        return False