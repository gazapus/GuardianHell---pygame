import pygame, random
from demon import Demon

class DemonFactory(pygame.sprite.Group):
     def __init__(self, quantity, demonPathImage, demonFallPathImage, speedX, speedY, lives):
          pygame.sprite.Group.__init__(self)
          pos_x = 400
          pos_y = 600
          for i in range(quantity):
               demon = Demon((pos_x, pos_y), demonPathImage, demonFallPathImage, [speedX, speedY], lives)  
               self.add(demon)
               pos_x = random.randint(round(demon.rect.width/2), 800 - round(demon.rect.width/2))
               pos_y = random.randint(pos_y, pos_y+200)
                