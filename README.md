📄 README.md
markdown

# libGML — Game Making Library

**libGML** is a lightweight 2D game engine for Python, built on top of Pygame.  
It provides ready-to-use tools for the most tedious parts of game development:  
rendering, tilemaps, camera, collisions, UI, interactables, and more.

**Version:** 1.0.0 (Final)  
**License:** MIT  
**Author:** ImPulseStory  
**GitHub:** https://github.com/ImPulseStory/libGML

---

## 🚀 Installation

```bash
pip install libGML

⚡ Quick Start
python

from libGML.graphics.sprite import Sprite
from libGML.input.keyboard import Keyboard
from libGML.core.world import World
from libGML.core.camera import Camera
import pygame

pygame.init()
sc = pygame.display.set_mode((800, 600))

keyboard = Keyboard()
sprites = Sprite()
world = World(sc)
camera = Camera()

# Load map and tileset
map = world.load_room_csv("map.csv")
tileset = pygame.image.load("tileset.png")
atlas = sprites.cutTileSet(tileset, 16, 16)
atlas = sprites.resizeTileset(atlas, 32, 32)

# Create player
player = sprites.create_sprite(100, 100, 32, 32)
texture = sprites.load_texture("player.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if keyboard.is_pressed("W"):
        player = sprites.move((0, -5), player)

    sc.fill((20, 20, 30))
    camera.follow(player, sc)
    world.draw_layer(map, atlas, 32, 32, camera)
    sprites.draw(sc, player, texture, camera)
    pygame.display.flip()

📖 Documentation

Full API documentation is available in DOCS.md.
🧩 Modules
Module	Description
graphics/sprite	Sprite creation, movement, drawing, tileset cutting
graphics/transform	Scale, rotate, flip surfaces
input/keyboard	Keyboard input handling
input/mouse	Mouse input handling (clicks, hover, release)
core/world	Tilemap loading, drawing, collisions, interactables
core/camera	Camera follow and coordinate conversion
core/vector2	2D vector math
uix/ui	UI container
uix/button	Clickable button
uix/label	Text label
uix/panel	Rectangular panel
uix/textinput	Text input field
🎮 Example Game

A full example game is available in the examples/ folder.
📜 License

MIT License. See LICENSE for details.
text


---

# 📄 DOCS.md (Full API)

```markdown
# libGML API Documentation — v1.0.0

## Table of Contents
1. [Sprite](#sprite)
2. [Transform](#transform)
3. [Keyboard](#keyboard)
4. [Mouse](#mouse)
5. [World](#world)
6. [Camera](#camera)
7. [Vector2](#vector2)
8. [UI](#ui)
9. [Button](#button)
10. [Label](#label)
11. [Panel](#panel)
12. [TextInput](#textinput)

---

## Sprite

**Module:** `libGML.graphics.sprite`

### `load_texture(filename)`
Loads an image from file.
```python
texture = sprites.load_texture("player.png")

create_sprite(x, y, width, height)

Creates a sprite as a pygame.Rect.
python

player = sprites.create_sprite(100, 100, 32, 32)

move(dest, rect)

Returns a new rect moved by (dx, dy).
python

new_rect = sprites.move((5, 0), player)

draw(surface, rect, texture, camera=None)

Draws the sprite. If camera is provided, applies camera offset.
python

sprites.draw(sc, player, texture, camera)

get_frame(frames, current_index, dt, delay=0.1, step=1)

Returns the next animation frame index.
python

key = sprites.get_frame(frames, key, dt, delay=0.5)

cutTileSet(tileset, width, height)

Cuts a tileset into a dictionary of tiles.
python

atlas = sprites.cutTileSet(tileset, 16, 16)

resizeTileset(atlas, width, height)

Scales all tiles in the atlas to a new size.
python

atlas = sprites.resizeTileset(atlas, 32, 32)

Transform

Module: libGML.graphics.transform
scale(dest, src)

Scales a surface to dest size.
python

texture = transform.scale((32, 32), texture)

rotate(angle, src)

Rotates a surface by angle degrees.
flip(surface, flip_x, flip_y)

Flips a surface horizontally/vertically.
Keyboard

Module: libGML.input.keyboard
is_pressed(key) -> bool

Returns True if the key is currently pressed.
python

if keyboard.is_pressed("W"):
    ...

update(events)

Updates internal state from events.
get_text_input() -> str

Returns accumulated text input.
clear_text_input()

Clears the text buffer.
Mouse

Module: libGML.input.mouse
update()

Updates mouse state. Call once per frame.
getPos() -> (x, y)

Returns mouse position.
is_hover(rect) -> bool

Returns True if the mouse is over the rect.
mouseLeftButtonDown() -> bool

Returns True if LMB is held.
mouseLeftButtonReleased() -> bool

Returns True on the frame LMB was released.
mouseLeftButtonClicked(rect) -> bool

Returns True if LMB was released over rect.

Same methods exist for middle and right buttons.
World

Module: libGML.core.world
load_room_csv(filename) -> list

Loads a CSV tilemap.
load_room_json(filename) -> dict

Loads a JSON tilemap.
draw_layer(map, atlas, width, height, camera)

Draws a tilemap layer with culling.
can_move_to(rect, tile_size, blocked_tiles, map) -> bool

Checks collision against blocked tiles.
add_interactable(tile_id, trigger="E")

Registers a tile as interactable.
check_interactables(player_rect, map, tile_size) -> bool

Returns True if the player is on an interactable tile and pressed the trigger key.
Camera

Module: libGML.core.camera
follow(rect, surface)

Centers the camera on the rect.
apply(x, y) -> (x, y)

Applies camera offset to coordinates.
Vector2

Module: libGML.core.vector2

Supports +, -, *, /, length(), normalized(), distance().
python

v = Vector2(3, 4)
print(v.length())  # 5.0

UI

Module: libGML.uix.ui
create_button(...)
create_label(...)
create_panel(...)
create_textInput(...)

Each returns the created element.
update(mouse, keyboard, events)

Updates all elements.
draw(screen)

Draws all elements.
Button

Module: libGML.uix.button

Clickable button with hover effect and on_click callback.
python

ui.create_button(100, 100, 200, 50, (50, 50, 200), "Start", start_game)

Label

Module: libGML.uix.label

Displays text.
python

ui.create_label(10, 10, 100, 30, (255, 255, 255), "HP: 100")

Panel

Module: libGML.uix.panel

Rectangular background.
python

ui.create_panel(0, 0, 800, 50, (30, 30, 40))

TextInput

Module: libGML.uix.textinput

Single-line text input with hint and on_enter callback.
python

ui.create_textInput(100, 200, 200, 40, (255, 255, 255), "Enter name", on_enter=submit)

License

MIT © ImPulseStory
text


---

# 📄 CHANGELOG.md

```markdown
# Changelog

## [1.0.0] — 2026-09-10
### Added
- `Mouse` class with full button state and click detection.
- `UI` system: `Button`, `Label`, `Panel`, `TextInput`.
- `World.add_interactable` and `check_interactables`.
- `Sprite.resizeTileset` for pre-scaled tiles.
- Full documentation and examples.

### Changed
- `World.draw_layer` now uses direct atlas lookup instead of iterating keys.
- Optimized tile rendering (no more `transform.scale` per frame).

### Fixed
- `Keyboard.keyses` dictionary (missing comma).
- `TextInput` deactivation on outside click.

---

## [0.3.0]
### Added
- CSV maps (`load_room_csv`).
- Tileset cutting (`cutTileSet`).
- Room transitions.

---

## [0.2.0]
### Added
- `Camera2D`.
- Animation (`get_frame`).
- `Vector2`.

---

## [0.1.0]
### Added
- Initial release: `Keyboard`, `Sprite`, `World`, `Transform`, collisions.

📄 LICENSE (MIT)
markdown

MIT License

Copyright (c) 2026 ImPulseStory

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Its all my friends! Just wait libGML based on LWJGL in Java!
