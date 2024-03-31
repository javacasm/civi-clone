# isometric game pretending to be civilization-clone

import pygame as pg
from config import *
from game import * 

v = 0.2
print(f'{__name__} MyCivi v{v}' )

def main():
    running = True 
    playing = True # Inside de game (not me menu)
    
    # init pygame
    pg.init()
    
    # create screen
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # pg.FULLSCREEN
    # init clock (for PFS)
    clock = pg.time.Clock()

    # create game
    game = Game(screen,clock)


    while running:
        
        # TODO: menús
        
        while playing:
            game.run()
        
if __name__ == '__main__':
    main()