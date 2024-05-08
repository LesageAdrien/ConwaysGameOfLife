import pygame as pg
import numpy as np

class GameOfLifeRenderer:
    def __init__(self):
        self.position = np.zeros(2).astype(float)
        self.scale = 1

        pg.init()
        self.screensize = np.array(pg.display.get_desktop_sizes()[0])
        self.screensize = self.screensize.min()*np.ones(2, dtype=float)-50
        self.window = pg.display.set_mode(self.screensize)
        pg.display.set_caption("Game Of Life")
        pg.display.set_icon(pg.surface.Surface((1, 1)))
        self.running = True

    def __del__(self):
        pg.quit()

    def move(self):
        return
    def disp(self, boolarray):
        self.window.fill((0, 0, 0))
        self.window.blit(pg.transform.scale(pg.surfarray.make_surface(boolarray.astype(float)*255), self.screensize), (0, 0))
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    def isRunning(self):
        return self.running

    def wait(self, time=0.1):
        pg.time.wait(int(time * 1000))

