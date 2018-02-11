import pygame
import mysqltest
from pygame import *
from pygame.locals import *
from pygame.sprite import *
import mysqltest
import billno
class Probe(Sprite):
    def __init__(self,x,y,image):
        Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.co=0
      
class display():
    def begin(self):
        pygame.init()
        screen=pygame.display.set_mode((740,480))
        image=pygame.image.load("images/image4.jpg")
        image2=pygame.image.load("done.png")
        image3=pygame.image.load("b.png")
        black=(0,0,0)
        myfont = pygame.font.SysFont("comicsansms",20)
        id = myfont.render("ID",4,black)
        p_name = myfont.render("Product name",4,black)
        price = myfont.render("Price",4,black)
        des = myfont.render("Description",4,black)
        while True:
            c=mysqltest.fetching_data()
            id1,pname1,price1,descrip=c.connect()
            screen.blit(image,(0,0))
            screen.blit(id,(35,15))
            screen.blit(p_name,(120,15))
            screen.blit(price,(320,15))
            screen.blit(des,(420,15))
            pygame.draw.line(screen,0,[10,0],[10,400],2)
            pygame.draw.line(screen,0,[100,0],[100,400],2)
            pygame.draw.line(screen,0,[300,0],[300,400],2)
            pygame.draw.line(screen,0,[400,0],[400,400],2)
            pygame.draw.line(screen,0,[600,0],[600,400],2)
            pygame.draw.line(screen,0,[10,400],[600,400],2)
            pygame.draw.line(screen,0,[10,0],[600,0],2)
            pygame.draw.line(screen,0,[10,50],[600,50],2)
            pygame.draw.line(screen,0,[10,100],[600,100],2)
            pygame.draw.line(screen,0,[10,150],[600,150],2)
            pygame.draw.line(screen,0,[10,200],[600,200],2)
            pygame.draw.line(screen,0,[10,250],[600,250],2)
            pygame.draw.line(screen,0,[10,300],[600,300],2)
            pygame.draw.line(screen,0,[10,350],[600,350],2)
            Group=pygame.sprite.Group()
            s=Probe(530,420,image2)
            q=Probe(30,400,image3)
            Group.add(s,q)
            x=0
            for i in range(0,len(id1)):
                           a1=myfont.render(str(id1[i]),3,black)
                           screen.blit(a1,(30,70+x))
                           a2=myfont.render(str(pname1[i]),3,black)
                           screen.blit(a2,(130,70+x))
                           a3=myfont.render(str(price1[i]),3,black)
                           screen.blit(a3,(320,70+x))
                           a4=myfont.render(str(descrip[i]),3,black)
                           screen.blit(a4,(420,70+x))
                           x+=50
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)

                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if s.rect.collidepoint(pygame.mouse.get_pos()):
                        d=mysqltest.fetching_data()
                        amount=d.delete()
                        f=billno.bill()
                        f.display(amount)
                    elif q.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit(0)

                    
            Group.draw(screen)
            pygame.display.flip()

