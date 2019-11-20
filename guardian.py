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

        def update(self, event, width):
                if(event.key == pygame.K_LEFT and self.rect.left > 0):
                        self.speed = [-7,0]
                        self.image = self.leftImage
                        self.directionRight = False
                elif(event.key == pygame.K_RIGHT and self.rect.right < width):
                        self.speed = [7,0]
                        self.image = self.rightImage
                        self.directionRight = True
                elif(event.key == pygame.K_SPACE):
                        self.attack()
                else:
                        self.speed = [0,0]
                self.rect.move_ip(self.speed)

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
                        timeAttack = Timer(0.4, self.noAttack)
                        timeAttack.start()
