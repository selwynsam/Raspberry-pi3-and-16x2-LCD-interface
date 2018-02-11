import pygame
import mysqltest
from pygame import *
from pygame.locals import *
from pygame.sprite import *
import mysqltest

class Probe(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.image=pygame.image.load("b.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.co=0

class bill():
    def display(self,amount):
        pygame.init()
        screen=pygame.display.set_mode((740,480))
        black=(0,0,0)
        myfont = pygame.font.SysFont("comicsansms",35)
        p_name = myfont.render('Gross amount',4,black)
        amount=str(amount)
        price = myfont.render(amount,4,black)
        Group=pygame.sprite.Group()
        f=Probe(530,400)
        Group.add(f)
        while True:
            screen.fill((255,255,255))
            screen.blit(p_name,(250,300))
            screen.blit(price,(480,300))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if f.rect.collidepoint(pygame.mouse.get_pos()):
                        import interface
                        z=interface.display()
                        z.begin()
            Group.draw(screen)            
            pygame.display.flip()
