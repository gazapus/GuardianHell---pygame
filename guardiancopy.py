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
                self.lives = lives
                self.isAttacking = False
                self.directionRight = False
                self.isJumping = False
                self.isResting = False
                self.jumpCount = 12   

        def moveRight(self, max):
                if(self.rect.right < max):
                        self.rect.x += 7
                        self.image = self.rightImage
                        self.directionRight = True
        
        def moveLeft(self, min):
                if(self.rect.left > min):
                        self.rect.x -= 7
                        self.image = self.leftImage
                        self.directionRight = False
                        
        def jump(self):
                if(not self.isJumping):
                        self.isJumping = True

        def update(self):
                if(self.isJumping and not self.isResting):
                        if self.jumpCount >= -12:
                                self.rect.y -= (self.jumpCount * abs(self.jumpCount))*0.1
                                self.jumpCount -= 1
                        else: 
                                self.jumpCount = 12
                                self.isJumping = False
                                self.isResting = True
                                restTime = Timer(0.2, self.finishBreak)
                                restTime.start()
                if(self.isAttacking):
                        self.image = self.rightAttackImage if self.directionRight else self.leftAttackImage
                else:
                        self.image = self.rightImage if self.directionRight else self.leftImage
                       
        def finishBreak(self):
                self.isResting = False

        def noAttack(self):
                self.isAttacking = False

        def attack(self):
                if(not self.isAttacking):
                        self.isAttacking = True
                        timeAttack = Timer(0.2, self.noAttack)
                        timeAttack.start()