# Pygame Project
# Author: Yuan Yuan

import pygame as pg
import random

# --CONSTANTS--
    # COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

#TODO: font

# Scale the image down
CURSOR = pg.image.load("./images/cursor.png")
CURSOR_LEFT = pg.transform.scale(
    CURSOR,
    (CURSOR.get_width() // 25, CURSOR.get_height() // 25)
)
CURSOR_RIGHT = pg.transform.flip(CURSOR_LEFT, True, False)

# Starting screen background
class Starting(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        start_image = pg.image.load("images/starting.png")
        start_image = pg.transform.scale(start_image, (1280, 720))

        self.rect = start_image.get_rect()

# Make the class for the player
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = CURSOR_RIGHT

        self.rect = self.image.get_rect()
        self.last_x = 0

    def update(self):
        """Follow the mouse"""
        cur_x = pg.mouse.get_pos()
        
        if self.last_x < cur_x[0]:
            self.image = CURSOR_RIGHT
        elif self.last_x > cur_x[0]:
            self.image = CURSOR_LEFT
    
        self.rect.center = cur_x

        self.last_x = pg.mouse.get_pos()[0]


# TODO: Make the class for the icing/cream
    # When clicked on will spawn onto the cake
# class Vanilla(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = van_cream
#         self.rect = self.image.get_rect()

# Spawn the image at one specific spot
# When clicked on will appear on the cake in the middle

# class Chocolate(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = choco_cream
#         self.rect = self.image.get_rect()

# class Strawberry(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = straw_cream
#         self.rect = self.image.get_rect()


# TODO: Make the class for the toppings
    # When clicked on will will spawn onto the cake on top of the icing/cream
# class Cherry(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = cherry
#         self.rect = self.image.get_rect()

# class Flakes(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = choco_flakes
#         self.rect = self.image.get_rect()

# class Straw(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = straw_berry
#         self.rect = self.image.get_rect()


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --VARIABLES--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # Display name
    pg.display.set_caption("Cake Maker")

    # --SPRITES--
    all_sprites = pg.sprite.Group()

    # Player sprite object
    player = Player()
    all_sprites.add(player)
    
    # Game start screen
    starting_bg =  Starting()
    all_sprites.add(starting_bg)
    

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()