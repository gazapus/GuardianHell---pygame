import pygame, time
from threading import Thread
from threading import Timer

class Guardian(pygame.sprite.Sprite):
        def __init__(self, startingPosition, lives):
                pygame.sprite.Sprite.__init__(self)
                self.rightImage =  pygame.image.load('guardian-r.png')
                self.leftImage =  pygame.image.load('guardian-l.png')
                self.leftAttackImage = pygame.image.load('guardian-l-a.png')
                self.rightAttackImage = pygame.image.load('guardian-r-a.png')
                self.image = self.rightImage
                self.rect = self.image.get_rect()
                self.rect.center = startingPosition
                self.speed = [0,0]
                self.lives = lives
                self.attacking = False
                self.directionRight = False
                self.jumping = False
                self.resting = False
                self.jumpCount = 12

        def update(self, event, width):
                if(event.key == pygame.K_LEFT and self.rect.left > 0):
                        self.speed = [-8,0]
                        self.image = self.leftImage
                        self.directionRight = False
                elif(event.key == pygame.K_RIGHT and self.rect.right < width):
                        self.speed = [8,0]
                        self.image = self.rightImage
                        self.directionRight = True
                elif(event.key == pygame.K_SPACE):
                        self.attack()
                elif(event.key == pygame.K_UP):
                        self.jumping = True
                        return 0
                else:
                        self.speed = [0,0]
                self.rect.move_ip(self.speed)
        
        def updateJump(self):
                if(self.jumping and not self.resting):
                        if self.jumpCount >= -12:
                                self.rect.y -= (self.jumpCount * abs(self.jumpCount))*0.1
                                self.jumpCount -= 1
                        else: 
                                self.jumpCount = 12
                                self.jumping = False
                                restTime = Timer(0.2, self.unrest)
                                self.resting = True
                                restTime.start()
        def unrest(self):
                self.resting = False

        def noAttack(self):
                if(self.directionRight):
                        self.image = self.rightImage
                else:
                        self.image = self.leftImage
                self.attacking = False

        def attack(self):
                if(not self.attacking):
                        self.speed = [0,0]      
                        self.attacking = True
                        if(self.directionRight):
                                self.image = self.rightAttackImage
                        else:
                                self.image = self.leftAttackImage
                        timeAttack = Timer(0.3, self.noAttack)
                        timeAttack.start()
