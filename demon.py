import pygame

class Demon(pygame.sprite.Sprite):
     def __init__(self, startingPosition, demonImagePath, demonFallImagePath, speed, resistance):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load(demonImagePath)
          self.fallingImage = pygame.image.load(demonFallImagePath)
          self.rect = self.image.get_rect()
          self.rect.center = startingPosition
          self.speed = speed
          self.resistance = resistance
          self.falling = False
          self.pointsShot = 10

     def update(self):
          if(self.rect.left <= 0 or self.rect.right >= 800):
               self.speed[0] = -self.speed[0]
          self.rect.move_ip(self.speed)

     def getAttack(self):
          points = 0
          if(not self.falling):
               self.speed[1] = self.speed[1] * 1.5
               self.speed[1] = - self.speed[1]
               self.speed[0] = 0
               self.falling = True
               self.image = self.fallingImage
               points = self.pointsShot
          return points