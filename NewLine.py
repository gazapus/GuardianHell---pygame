import pygame

class Line(pygame.sprite.Sprite):
     def __init__(self, width, altitude):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.Surface([width, 1])
          self.rect = self.image.get_rect()
          self.rect.center = (width/2, altitude)