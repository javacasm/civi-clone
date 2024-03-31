import pygame as pg
import random
from config import *
from utils  import * 

v = 0.2
print(f'{__name__} v{v}')

class World():
    def __init__(self,nx_tile,ny_tile):
        self.nx_tile = nx_tile
        self.ny_tile = ny_tile
        self.images = self.load_images()        
        self.world = self.generate_world()

    def generate_world(self):
        world = [] # list of lists (bidimensional)
        # every tile will be a dictionary with position (pixels), type and all the data needed
        for grid_x in range(self.nx_tile):
            world.append([]) # new list por every x
            for grid_y in range(self.ny_tile):
                world_tile = self.create_tile(grid_x, grid_y)
                world[grid_x].append(world_tile)

        return world

    def create_tile(self, grid_x, grid_y):
        # pixel cartessian rect
        cartessian_rect = [ (grid_x * TILE_SIZE , grid_y * TILE_SIZE),
                            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
                            (grid_x * TILE_SIZE + TILE_SIZE , grid_y * TILE_SIZE + TILE_SIZE),
                            (grid_x * TILE_SIZE , grid_y * TILE_SIZE + TILE_SIZE) ]
        
        # pixel isometric rect
        isometric_poly = [cartessian_to_isometric(x, y) for x, y in cartessian_rect]
        
        # position for render
        minx = min([x for x, y in isometric_poly])
        miny = min([y for x, y in isometric_poly])

        r = random.randint(1, 100)
        
        tile_z = 0
        
        if r < 3:
            tile = "flower"
        elif r <= 10:
            tile_z = 5
            tile = "water"
        elif r <= 20:
            tile = "rock"
            tile_z = 8
        else:
            tile = "grass"
            tile_z = 10
        
        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": cartessian_rect,
            "iso_poly": isometric_poly,
            "render_pos": [minx, miny],
            "tile_z": tile_z,
            "tile": tile
        }

        return out        
    
    def load_images(self):

        flower = pg.image.load("assets/graphics/tile_041.png")
        water = pg.image.load("assets/graphics/tile_104.png")
        rock = pg.image.load("assets/graphics/tile_063.png")
        grass = pg.image.load("assets/graphics/tile_040.png")
        
        return {"flower": flower, "water": water, "rock": rock,"grass": grass}