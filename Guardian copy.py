import pygame, time
from threading import Thread
from threading import Timer
from Demon import Demon

class Guardian(pygame.sprite.Sprite):
        def __init__(self, asset, positionX, positionY, lives, initialPoints):
                pygame.sprite.Sprite.__init__(self)
                self.rightImage =  pygame.image.load('./src/images/guardian-r.png')
                self.leftImage =  pygame.image.load('./src/images/guardian-l.png')
                self.leftAttackImage = pygame.image.load('./src/images/guardian-l-a.png')
                self.rightAttackImage = pygame.image.load('./src/images/guardian-r-a.png')
                self.image = self.rightImage
                self.rect = self.image.get_rect()
                self.rect.x = positionX
                self.rect.y = positionY
                self.lives = lives
                self.isAttacking = False
                self.directionRight = False
                self.isJumping = False
                self.isResting = False
                self.jumpCount = 12
                self.isRestingAttack = False
                self.damageHit = 1
                self.points = initialPoints

        def moveRight(self, max):
                if(self.rect.right < max and not self.isAttacking):
                        self.rect.x += 7
                        self.image = self.rightImage
                        self.directionRight = True
        
        def moveLeft(self, min):
                if(self.rect.left > min and not self.isAttacking):
                        self.rect.x -= 7
                        self.image = self.leftImage
                        self.directionRight = False
                        
        def jump(self):
                if(not self.isJumping):
                        self.isJumping = True

        def update(self):
                if(self.isJumping and not self.isResting):
                        if self.jumpCount >= -12:
                                self.rect.y -= (self.jumpCount * abs(self.jumpCount))*0.1       #error parchado
                                self.jumpCount -= 1
                        else: 
                                self.rect.y += 11       #parche: le suma los 11 pixeles que se adelanta en cada salto
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

        def finishBreakAttack(self):
                self.isRestingAttack = False

        def finishAttack(self):
                self.isAttacking = False
                self.isRestingAttack = True
                restTimeAttack = Timer(0.3, self.finishBreakAttack)
                restTimeAttack.start()

        def attack(self, demonsAttacked):
                if(not self.isRestingAttack and not self.isAttacking):
                        self.isAttacking = True
                        timeAttack = Timer(0.2, self.finishAttack)
                        timeAttack.start()
                        if(demonsAttacked):
                                for demon in demonsAttacked:
                                        self.points += demon.getAttack(self.damageHit)

        def takeTreasure(self, treasuresTaken):
                if(treasuresTaken):
                        for treasure in treasuresTaken:
                                self.points += treasure.points
                                treasure.beTaken()