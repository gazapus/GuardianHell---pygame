import pygame, time
from threading import Timer
from Enemy import Demon
from Item import Item
from itertools import cycle

class Guardian(pygame.sprite.Sprite):
     def __init__(
               self, runLeftImagesPath, stoppedLeftImagePath, jumpLeftImagePath, attackImagePath, 
               soundPaths, startingPosition, _lives, _points
               ):
          pygame.sprite.Sprite.__init__(self)
          pygame.mixer.init
          self.runLeftImages =  self.setImages(runLeftImagesPath)
          self.runRightImages = self.setInvertedImages(runLeftImagesPath)
          self.stoppedLeftImage = pygame.image.load(stoppedLeftImagePath)
          self.stoppedRightImage = pygame.transform.flip(self.stoppedLeftImage, True, False)
          self.leftJumpImage = pygame.image.load(jumpLeftImagePath)
          self.rightJumpImage = pygame.transform.flip(self.leftJumpImage, True, False)
          self.leftAttackImage = pygame.image.load(attackImagePath)
          self.rightAttackImage = pygame.transform.flip(self.leftAttackImage, True, False)
          self.image = self.stoppedLeftImage
          self.attackSound = pygame.mixer.Sound(soundPaths['attack'])
          self.scream = pygame.mixer.Sound(soundPaths['demonScream'])
          self.rect = self.image.get_rect()
          self.rect.center = startingPosition
          self.lives = _lives
          self.damageHit = 1
          self.points = _points
          self.lastXPosition = startingPosition[0]
          self.orientationLeft = True
          self.isJumping = False
          self.isRestingJump = False
          self.jumpCount = 15
          self.isAttacking = False
          self.canAttack = True
          self.attackStarted = False
          self.leftAttackedImage = pygame.image.load('./src/images/guardian/__demon_hurt_no_flames_000.png')
          self.rightAttackedImage = pygame.transform.flip(self.leftAttackedImage, True, False)
          self.isBeingAttacked = False
               
     def setImages(self, imagesPath):
          """
          Return a cyclic images list
          :param list images: list of paths of images
          """
          imagesList = []
          for imagePath in imagesPath:
               imagesList.append(pygame.image.load(imagePath).convert_alpha())
          return cycle(imagesList)
     
     def setInvertedImages(self, imagesPath):
          imagesList = []
          for imagePath in imagesPath:
               currentImage = pygame.image.load(imagePath).convert_alpha()
               currentImage = pygame.transform.flip(currentImage, True, False)
               imagesList.append(currentImage)
          return cycle(imagesList)

     def moveLeft(self, min):
          if(self.isAttacking):
               return
          if(not self.orientationLeft):
               self.image = next(self.runLeftImages)
               self.orientationLeft = True
          if(self.rect.left > min):
               self.rect.x -= 9
               if(self.rect.x <= self.lastXPosition - 40):
                    self.image = next(self.runLeftImages)
                    self.lastXPosition = self.rect.x
          else:
               self.image = self.stoppedLeftImage
     
     def moveRight(self, max):
          if(self.isAttacking):
               return
          if(self.orientationLeft):
               self.image = next(self.runRightImages)
               self.orientationLeft = False
          if(self.rect.right < max - 40):    #el menos 40 es parche, luego ver redefinir el rec cada cambio de img
               self.rect.x += 9
               if(self.rect.x >= self.lastXPosition + 40):
                    self.image = next(self.runRightImages)
                    self.lastXPosition = self.rect.x
          else:
               self.image = self.stoppedRightImage

     def stopWalk(self):
          if not(self.isJumping or self.isAttacking ):
               self.image = self.stoppedLeftImage if self.orientationLeft else self.stoppedRightImage

     def jump(self):
          if(not self.isJumping and not self.isRestingJump):
               self.isJumping = True

     def update(self):
          if(self.isJumping):
               if self.jumpCount >= -15:
                    self.image = self.leftJumpImage if self.orientationLeft else self.rightJumpImage
                    self.rect.y -= (self.jumpCount * abs(self.jumpCount))*0.1       
                    self.jumpCount -= 1
               else: 
                    self.rect.y += 14     #parche: le suma los pixeles que se adelanta en cada salto
                    self.jumpCount = 15
                    self.isJumping = False
                    self.isRestingJump = True
                    Timer(0.2, self.finishJumpBreak).start()
          if(self.isAttacking):
               self.image = self.leftAttackImage if self.orientationLeft else self.rightAttackImage
          if(self.isBeingAttacked):
               self.image = self.leftAttackedImage if self.orientationLeft else self.rightAttackedImage
         
     def finishJumpBreak(self):
          self.isRestingJump = False

     def attack(self, enemiesAttacked=[]):
          if(self.canAttack):
               if(not self.attackStarted):
                    self.attackStarted = True
                    self.attackSound.play()
                    self.isAttacking = True  
                    diff = -100 if self.orientationLeft else 30
                    self.rect.move_ip(diff, 0)
                    self.rect.inflate_ip(0, -15)
                    Timer(0.2, self.finishAttack, [diff]).start()   #en este tiempo queda inhabilitado para atacar
               if(enemiesAttacked):
                    for enemy in enemiesAttacked:
                         self.points += enemy.getAttack(self.damageHit)

     def finishBreakAttack(self):
          self.canAttack = True
          self.attackStarted = False

     def finishAttack(self, diff):
          self.rect.move_ip(-diff, 0)
          self.rect.inflate_ip(0, 15)
          self.isAttacking = False
          self.canAttack = False
          Timer(0.3, self.finishBreakAttack).start()
          self.image = self.stoppedLeftImage if self.orientationLeft else self.stoppedRightImage
        
     def getTreasure(self, treasuresTaken):
          if(treasuresTaken):
               for treasure in treasuresTaken:
                    self.points += treasure.beTaken()

     def getAttack(self, attacksTaken):
          if(attacksTaken):
               if(not self.isBeingAttacked):
                    self.scream.play()
               for attack in attacksTaken:
                    self.lives -= attack.beTaken()
               self.isBeingAttacked = True
               Timer(0.2, self.finishAttacked).start()

     def finishAttacked(self):
          self.isBeingAttacked = False
          self.image = self.stoppedLeftImage if self.orientationLeft else self.stoppedRightImage

     def getLives(self, livesTaken):
          if(livesTaken):
               for live in livesTaken:
                    self.lives += live.beTaken()              
