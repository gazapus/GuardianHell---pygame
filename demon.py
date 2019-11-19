import pygame

class Demon(pygame.sprite.Sprite):
     def __init__(self, startingPosition, demonPath, speed, resistance):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load(demonPath)
          self.rect = self.image.get_rect()
          self.rect.center = startingPosition
          self.speed = speed
          self.resistance = resistance
          self.falling = False

     def update(self):
          self.rect.move_ip(self.speed)

     def getAttack(self):
          if(self.falling == False):
               self.speed[1] = - self.speed[1]
               self.falling = True