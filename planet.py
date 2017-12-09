import pygame,math
from pygame import *
from math import *

class WindowInit():
    def __init__(self,NameCaption="Solar System"):
        pygame.display.set_caption(NameCaption)

class Planet(WindowInit):
    def __init__(self,x,y,color,radius):
        super().__init__()
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
    def render(self):
        draw.circle(screen,Color(self.color),((int(self.x),int(self.y))),self.radius)

class RunPlanet(Planet):
    def __init__(self,x,y,color,radius,vx,vy,delay):
        super().__init__(x,y,color,radius)
        self.vx=vx
        self.vy=vy
        self.delay=delay
    def MovePlanet(self):
        screen.fill((50, 50, 50))
        r = sqrt((self.x - 400) ** 2 + (self.y - 400) ** 2)
        ax = self.delay * 1000 * (400 - self.x) / r ** 3
        ay = self.delay * 1000 * (400 - self.y) / r ** 3
        self.vx += ax
        self.vy += ay
        self.x += self.vx
        self.y += self.vy

def Intersect(x1,x2,y1,y2,r1,r2):
    if x2 < x1 + 2 * r1 and x2 > x1 - 2 * r2 and y2 < y1 + 2 * r1 and y2 > y1 - 2 * r2:
        return 1
    else:
        return 0



window = pygame.display.set_mode((800, 800))
screen = pygame.Surface((800, 800))

Sun = Planet(400,400,"yellow",20)
Mercury=RunPlanet(50,300,"green",5,0.5,1,1)
Mercury.crash= False
Venera=RunPlanet(250,200,"blue",8,1,-2,3)
Venera.crash= False
Mars=RunPlanet(500,500,"red",10,-1,4,4)
Mars.crash= False

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    # if Intersect(Sun.x,Mars.x,Sun.y,Mars.y,Sun.radius,Mars.radius):
    #     Mars.crash= True
    #     Mars.radius=0
    # else:
    #     Mars.crash= False
    #
    # if Intersect(Sun.x,Mercury.x,Sun.y,Mercury.y,Sun.radius,Mercury.radius):
    #     Mercury.crash= True
    #     Mercury.radius=0
    # else:
    #     Mercury.crash= False
    #
    # if Intersect(Sun.x,Venera.x,Sun.y,Venera.y,Sun.radius,Venera.radius):
    #     Venera.crash= True
    #     Venera.radius=0
    # else:
    #     Venera.crash= False

    Mars.MovePlanet()
    Venera.MovePlanet()
    Mercury.MovePlanet()
    Mercury.render()
    Venera.render()
    Mars.render()
    Sun.render()

    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(10)
