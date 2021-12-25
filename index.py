import sys
import pygame as pg


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 200)

SIZE = W, H = 500, 500

pg.init()
win = pg.display.set_mode(SIZE)


class Circle:
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
    
    def drawing(self):
        pg.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.y -= 1 
        elif keys[pg.K_DOWN]:
            self.y += 1 
        elif keys[pg.K_RIGHT]:
            self.x += 1 
        elif keys[pg.K_LEFT]:
            self.x -= 1 


my_circle = Circle(W // 2, H // 2, 70, GREEN)


def check_close():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


def drawing():
    win.fill(WHITE)
    my_circle.drawing()
    pg.display.update()


while True:
    check_close()
    my_circle.move()
    drawing()


# comment
