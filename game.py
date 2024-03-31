import pygame as pg
import sys
from world import World
from config import *

v = 0.2
print(f'{__name__} v{v}')

class Game():
    
    def __init__(self,screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        
        self.world = World(N_TILE,N_TILE)
        
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self._events()
            self._update()
            self._draw()
    
    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
    
    def _update(self):
        pass
    
    def _draw(self):
        self.screen.fill((0, 0, 0))
        for x in range(self.world.nx_tile):
            for y in range(self.world.ny_tile):
                if DEBUG:
                    sq = self.world.world[x][y]["cart_rect"]
                    rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                    pg.draw.rect(self.screen, (0, 0, 255), rect, 1)

                    p = self.world.world[x][y]["iso_poly"]
                    p = [(x + self.width/2, y + self.height/4) for x, y in p]
                    pg.draw.polygon(self.screen, (255, 0, 0), p, 1)
                                    
                render_pos =  self.world.world[x][y]["render_pos"]
                
                tile = self.world.world[x][y]["tile"]
                if tile != "":
                    self.screen.blit(self.world.images[tile],
                                    (render_pos[0] + self.width/2,
                                     self.world.world[x][y]["tile_z"]+render_pos[1] + self.height/4 - (self.world.images[tile].get_height() - TILE_SIZE)))
                
        pg.display.flip()
        