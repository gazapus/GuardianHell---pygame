import pygame, time
from threading import Thread
from threading import Timer
from Demon import Demon
from itertools import cycle

class Guardian(pygame.sprite.Sprite):
     def __init__(
               self, runLeftImagesPath, stoppedLeftImagePath, jumpLeftImagePath, attackImagePath,
               attackSoundPath, startingPosition, _lives, _points
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
          self.attackSound = pygame.mixer.Sound(attackSoundPath)
          self.rect = self.image.get_rect().inflate(-10, 00)
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
          self.isRestingAttack = False
               
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
          if(self.rect.right < max - 40):    #el menos 15 es parche, luego ver redefinir el rec cada cambio de img
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
         
     def finishJumpBreak(self):
          self.isRestingJump = False

     def finishBreakAttack(self):
          self.isRestingAttack = False

     def finishAttack(self):
          self.isAttacking = False
          self.isRestingAttack = True
          Timer(0.3, self.finishBreakAttack).start()
          self.image = self.stoppedLeftImage if self.orientationLeft else self.stoppedRightImage


     def attack(self):
          if(not self.isRestingAttack and not self.isAttacking):
               self.attackSound.play()
               self.isAttacking = True
               Timer(0.4, self.finishAttack).start()
