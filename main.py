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

    # Piping tubes
van_tube = pg.image.load("./images/van_tube.png")
choco_tube = pg.image.load("./images/choco_tube.png")
straw_tube = pg.image.load("./images/straw_tube.png")

    # Creams
van_cream = pg.image.load("./images/van_cream.png")
choco_cream = pg.image.load("./images/choco_cream.png")
straw_cream = pg.image.load("./images/straw_cream.png")

    #TODO: Toppings on table
# cherry = pg.image.load("./images/")
# choco_flakes = pg.image.load("./images/")
# straw_berry = pg.image.load("./images/")\

    #TODO: Toppings on cake
# cherry_top = pg.image.load("./images/")
# choco_top = pg.image.load("./images/")
# straw_top = pg.image.load("./images/")


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
        self.image = pg.transform.scale(start_image, (1280, 720))

        self.rect = self.image.get_rect()


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


# Class for the piping tubes
class Vanilla(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = van_tube
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 20, 430

        self.clicked = False

class Chocolate(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = choco_tube
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 130, 400

        self.clicked = False

class Strawberry(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = straw_tube
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 250, 370

        self.clicked = False



# TODO: Class for the toppings
    # When clicked on will will spawn onto the cake on top of the icing/cream
# class Cherry(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = cherry
        # self.rect = self.image.get_rect()
        # self.rect.x, self.rect.y = x, 430

        # self.clicked = False

# class Flakes(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = choco_flakes
        # self.rect = self.image.get_rect()
        # self.rect.x, self.rect.y = x, 400

        # self.clicked = False

# class Straw(pg.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image = straw_berry
        # self.rect = self.image.get_rect()
        # self.rect.x, self.rect.y = x, 370

        # self.clicked = False



def display_start_screen(screen: pg.Surface):
    """Display the start screen"""
    sprites = pg.sprite.Group()
    sprites.add(Starting())

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return
        
        sprites.draw(screen)

        pg.display.flip()
        


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --VARIABLES--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    background = pg.image.load("./images/bg.png")
    cake = pg.image.load("./images/cake.png")

    # Display name
    pg.display.set_caption("Cake Maker")

    # --SPRITES--
    all_sprites = pg.sprite.Group()
    tube_sprites = pg.sprite.Group()

    # Player sprite object
    player = Player()
    all_sprites.add(player)

    # Vanilla tube
    vanilla_tube = Vanilla()
    all_sprites.add(vanilla_tube)
    tube_sprites.add(vanilla_tube)

    # Choco tube
    choco_tube = Chocolate()
    all_sprites.add(choco_tube)
    tube_sprites.add(choco_tube)

    # Strawberry tube
    strawberry_tube = Strawberry()
    all_sprites.add(strawberry_tube)
    tube_sprites.add(strawberry_tube)

    # Starting screen
    display_start_screen(screen)

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            if event.type == pg.MOUSEBUTTONDOWN:
                for tube in tube_sprites:
                    if tube.rect.collidepoint(pg.mouse.get_pos()):
                        tube.clicked = True
                    

        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.blit(background, (0, 0))
        screen.blit(cake, (450, 200))

        if vanilla_tube.clicked:
            screen.blit(van_cream, (450, 150))

        if choco_tube.clicked:
            screen.blit(choco_cream, (448, 148))

        if strawberry_tube.clicked:
            screen.blit(straw_cream, (446, 150))

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()
