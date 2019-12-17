import pygame

class Line(pygame.sprite.Sprite):
     """
     objects that leave the playable area of the level
     """
     def __init__(self, width, altitude):
          """
          param width: width of the line
          param altitude: line position on the y axis
          """
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.Surface([width, 1])
          self.rect = self.image.get_rect()
          self.rect.center = (width/2, altitude)