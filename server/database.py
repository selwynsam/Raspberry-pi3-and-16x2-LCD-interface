import pygame
import mysqltest
from pygame import *
from pygame.locals import *
from pygame.sprite import *
import mysqltest
import billno
class Probe(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=pygame.image.load("b.png")
        self.rect=self.image.get_rect()
        self.rect.x=530
        self.rect.y=400
        self.run=True
        self.co=0
      
class display1():
    def begin(self):
        pygame.init()
        screen=pygame.display.set_mode((740,800))
        black=(0,0,0)
        image=pygame.image.load("images/image4.jpg")
        myfont = pygame.font.SysFont("comicsansms",20)
        quantity = myfont.render("ID",4,black)
        p_name = myfont.render("Product_name",4,black)
        price = myfont.render("Price",4,black)
        des = myfont.render("Description",4,black)
        loop=True
        while loop:
            a=mysqltest.fetching_data()
            a,b,c,d=a.display()
            screen.blit(image,(0,0))
            screen.blit(p_name,(25,15))
            screen.blit(price,(230,15))
            screen.blit(des,(350,15))
            screen.blit(quantity,(560,15))
            pygame.draw.line(screen,0,[210,0],[210,400],2)
            #pygame.draw.line(screen,0,[100,0],[100,400],2)
            pygame.draw.line(screen,0,[320,0],[320,400],2)
            pygame.draw.line(screen,0,[540,0],[540,400],2)
            pygame.draw.line(screen,0,[700,0],[700,400],2)
            pygame.draw.line(screen,0,[10,400],[700,400],2)
            pygame.draw.line(screen,0,[10,0],[700,0],2)
            
            Group=pygame.sprite.Group()
            s=Probe()
            Group.add(s)
            x=0
            for i in range(len(a)):
                           a1=myfont.render(str(b[i]),3,black)
                           screen.blit(a1,(30,70+x))
                           a2=myfont.render(str(c[i]),3,black)
                           screen.blit(a2,(230,70+x))
                           a3=myfont.render(str(d[i]),3,black)
                           screen.blit(a3,(350,70+x))
                           a4=myfont.render(str(a[i]),3,black)
                           screen.blit(a4,(550,70+x))
                           pygame.draw.line(screen,0,[10,100+x],[700,100+x],2)
                           x+=50
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)

                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if s.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit(0)
                    
            Group.draw(screen)
            pygame.display.flip()
        pygame.quit()
