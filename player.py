import pygame

ima_player = 'images/ting.png'
ima_player2 = 'images/dong.png'

class Player():
    def __init__(self,bg_size):
        #self.image = pygame.image.load('0.png').convert_alpha()  #图像 

        self.imageyou = pygame.image.load(ima_player)
        self.imagezuo = pygame.image.load(ima_player2)

        self.rect = self.imageyou.get_rect()    #位置
        self.bgwidth,self.bgheight = bg_size[0],bg_size[1]
        self.rect.left,self.rect.top = self.bgwidth/2,self.bgheight/2

        self.speed = 6       #速度
        self.x = self.rect.width
        self.y = self.rect.height

    def moveup(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0  #出界
            
    def movedown(self):
        if self.rect.bottom < self.bgheight:
            self.rect.top += self.speed
            '''
            self.imagezuo = pygame.transform.scale(self.imagezuo,(self.x,self.y))
            self.imageyou = pygame.transform.scale(self.imageyou,(self.x,self.y))
            self.x+=5
            self.y+=7
            '''
        else:
            self.rect.bottom = self.bgheight
            
    def moveleft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed

    def moveright(self):
        if self.rect.right < self.bgwidth:
            self.rect.left += self.speed

            
