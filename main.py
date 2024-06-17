# Pygame Project
# Author: Yuan Yuan

import pygame as pg
from pygame import mixer

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

    # Toppings on table
cherry = pg.image.load("./images/cherry_top.png")
choco_flakes = pg.image.load("./images/flake_jar.png")
straw_berry = pg.image.load("./images/straw_berry.png")

    #Toppings on cake
cherry_top = pg.image.load("./images/cherry.png")
choco_top = pg.image.load("./images/choco_flakes.png")
straw_top = pg.image.load("./images/berry.png")

# Scale the image down
CURSOR = pg.image.load("./images/cursor.png")
CURSOR_LEFT = pg.transform.scale(
    CURSOR,
    (CURSOR.get_width() // 25, CURSOR.get_height() // 25)
)
CURSOR_RIGHT = pg.transform.flip(CURSOR_LEFT, True, False)

end_pic = pg.image.load("./images/end_pop.png")
ok_pic = pg.image.load("./images/ok.png")
start_pic = pg.image.load("./images/start_pop.png")



# Starting screen display image
class Starting(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        start_image = pg.image.load("images/starting.png")
        self.image = pg.transform.scale(start_image, (1280, 720))

        self.rect = self.image.get_rect()


# Make the class for the player
class Player(pg.sprite.Sprite):
    """Cursor controlled by the player"""
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
    """Display the vanilla piping tube"""
    def __init__(self):
        super().__init__()

        self.image = van_tube
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 20, 430

        self.clicked = False

class Chocolate(pg.sprite.Sprite):
    """Display the chocolate piping tube"""
    def __init__(self):
        super().__init__()

        self.image = choco_tube
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 130, 400

        self.clicked = False

class Strawberry(pg.sprite.Sprite):
    """Display the strawberry piping tube"""
    def __init__(self):
        super().__init__()

        self.image = straw_tube
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 250, 370

        self.clicked = False


class TubeSprites(pg.sprite.Group):
    """Clicks the tube and unclicks the others."""
    def click(self, tube):
        for t in self.sprites():
            if t is not tube:
                t.clicked = False
            else:
                t.clicked = True

class Topping(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.clicked = False

    def click(self):
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True

# Class for the toppings
    # When clicked on will will spawn onto the cake on top of the icing/cream
class Cherry(Topping):
    """Display the Cherry topping"""
    def __init__(self):
        super().__init__()

        self.image = cherry
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 990, 410

class Flakes(Topping):
    """Display the Chocolate flakes topping"""
    def __init__(self):
        super().__init__()

        self.image = choco_flakes
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 1125, 430

class Straw(Topping):
    """Display the strawberry topping"""
    def __init__(self):
        super().__init__()

        self.image = straw_berry
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 850, 370


# Starting Screen display
def display_start_screen(screen: pg.Surface):
    """Display the start screen
    
    Returns:
        False if quitting"""
    sprites = pg.sprite.Group()
    sprites.add(Starting())

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return True
        
        sprites.draw(screen)

        pg.display.flip()
        

class Pop_up(pg.sprite.Sprite):
    """Display instruction image"""
    def __init__(self):
        super().__init__()

        self.image = start_pic
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 425, 140


class Button(pg.sprite.Sprite):
    """"For when the OK button"""
    def __init__(self):
        super().__init__()

        self.clicked = False

    def click(self):
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True


class Ok_button(Button):
    """OK button displayed on screen that shows prompt when clicked"""
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./images/ok.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 540, 20

        self.clicked = False



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
    tube_sprites = TubeSprites()
    topping_sprites = pg.sprite.Group()
    
    ok_button = Ok_button()
    all_sprites.add(ok_button)

    start_popup = Pop_up()
    all_sprites.add(start_popup)

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

    # Cherry topping
    cherry_topping = Cherry()
    all_sprites.add(cherry_topping)
    topping_sprites.add(cherry_topping)

    # Strawberry topping
    strawberry_topping = Straw()
    all_sprites.add(strawberry_topping)
    topping_sprites.add(strawberry_topping)

    # Chocolate flakes
    chocolate_flakes = Flakes()
    all_sprites.add(chocolate_flakes)
    topping_sprites.add(chocolate_flakes)

    # Player sprite object
    player = Player()
    all_sprites.add(player)

    # Starting screen
    if not display_start_screen(screen):
        done = True


    # Background music
    pg.mixer.init()
    bgmusic = pg.mixer.Sound("./sounds/ftp.ogg")
    bgmusic.play()
    

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            if event.type == pg.MOUSEBUTTONDOWN:
                for tube in tube_sprites:
                    if tube.rect.collidepoint(pg.mouse.get_pos()):
                        tube_sprites.click(tube)
                
                for topping in topping_sprites:
                    if topping.rect.collidepoint(pg.mouse.get_pos()):
                        topping.click()
                
                if ok_button.rect.collidepoint(pg.mouse.get_pos()):
                    ok_button.click()

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and start_popup:
                all_sprites.remove(start_popup)
                del(start_popup)
                start_popup = False
            
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and ok_button.clicked:
                return True
             

        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.blit(background, (0, 0))
        screen.blit(cake, (450, 200))

        #   If piping tubes are clicked the cream pops up on cake
        if vanilla_tube.clicked:
            screen.blit(van_cream, (450, 150))

        if choco_tube.clicked:
            screen.blit(choco_cream, (448, 148))

        if strawberry_tube.clicked:
            screen.blit(straw_cream, (446, 150))

        #   If toppings clicked it pops up on cake
        if cherry_topping.clicked:
            screen.blit(cherry_top, (450, 150))

        if chocolate_flakes.clicked:
            screen.blit(choco_top, (450, 150))

        if strawberry_topping.clicked:
            screen.blit(straw_top, (450, 150))

        if ok_button.clicked:
            screen.blit(end_pic, (425, 200))
        



        # Draw all sprites on the screen
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps
    

def main():
    # janky fix but it works
    while start():
        start()


if __name__ == "__main__":
    main()
